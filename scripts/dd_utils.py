# add:
# release date
# version
# smash database release
# sourmash version
# add num species, num genomes?
# taxonomy type (normal, lins, ??)
# "learn" sha256? or calc once & store? detect changes?

import os


class Params:
    def __init__(self, *, ksize, moltype, scaled):
        self.ksize = int(ksize)
        self.moltype = moltype
        self.scaled = int(scaled)
        self._validate()

    def _validate(self):
        assert self.ksize >= 4, self.ksize
        assert self.ksize <= 101, self.ksize

        assert self.moltype in {
            "DNA",
            "protein",
            "skip_m1n3",
            "skip_m2n3",
            "dayhoff",
            "hp",
        }, (moltype, self.moltypes)

        assert self.scaled >= 1, self.scaled
        assert self.scaled <= 1e9, self.scaled


class Taxonomy:
    def __init__(
        self, *, short, title, description, source, lineage_file, download_url
    ):
        self.short = str(short)
        self.title = str(title)
        self.description = str(description)
        self.source = str(source)
        self.lineage_file = lineage_file
        self.download_url = self.download_url = download_url.format(
            filename=lineage_file
        )

    def _validate(self):
        assert self.source in ["ncbi", "gtdb", "ictv", "lins"]

    def json(self):
        return self.__dict__

    def from_json(self, s):
        self.__dict__.update(json.loads(s))


class GenomeCollection:
    def __init__(
        self, *, short, title, description, category, sources, links, taxonomies
    ):
        self.short = str(short)
        self.title = str(title)
        self.description = str(description)
        self.sources = list(sources)
        self.category = str(category)
        self.links = list(links)
        self.taxonomies = list(taxonomies)
        self.sketches = []

        self._validate()

    def _validate(self):
        assert set(self.sources).issubset({"ncbi", "gtdb", "atb"}), self.sources
        assert self.category in ("bac+arc", "euk", "viruses"), self.category

        for descr, url in self.links:
            assert url.startswith("http://") or url.startswith("https://"), url

        for t in self.taxonomies:
            assert isinstance(t, Taxonomy)

    def json(self):
        d = dict(self.__dict__)
        d["taxonomies"] = [t.json() for t in self.taxonomies]
        return d

    def from_json(self, s):
        self.__dict__.update(json.loads(s))


class ConcreteSketchDatabase:
    def __init__(self, *, ksize, moltype, scaled, parent):
        self.ksize = ksize
        self.moltype = moltype
        self.scaled = scaled
        self.fmt = parent.fmt
        self.description = parent.description

        format_d = dict(
            ksize=ksize, moltype=moltype, moltype_l=moltype.lower(), scaled=scaled
        )
        self.filename = parent.filename.format(**format_d)

        format_d["filename"] = self.filename
        self.download_url = parent.download_url.format(**format_d)

    @property
    def basename(self):
        return os.path.basename(self.filename)


class SketchDatabases:
    def __init__(
        self,
        *,
        short,
        description,
        collection,
        params,
        fmt,
        index_type,
        download_url,
        filename,
    ):
        assert isinstance(collection, GenomeCollection)
        self.collection = collection

        self.short = str(short)
        self.description = str(description)
        self.params = params
        self.fmt = fmt
        self.index_type = index_type
        self.filename = str(filename)
        self.download_url = str(download_url)

        self._validate()
        self.collection.sketches.append(self)

    def _validate(self):
        assert self.fmt in {"zip", "tar.gz"}
        assert self.index_type in {"zipfile", "lca.json", "rocksdb"}

    def __getattr__(self, name):
        print(name)
        if name in self.__dict__:
            return self.__dict__[name]
        elif not name.startswith("_"):
            if name.startswith("k"):
                ksize = int(name[1:])
                if ksize in self.ksizes:
                    return ConcreteSketchDatabase(
                        ksize=ksize, moltype="DNA", parent=self
                    )
        raise AttributeError

    @property
    def files(self):
        for param in self.params:
            ksize = param.ksize
            scaled = param.scaled
            moltype = param.moltype
            yield ConcreteSketchDatabase(
                ksize=ksize, moltype=moltype, scaled=scaled, parent=self
            )

    def json(self):
        d = dict(self.__dict__)
        d["collection"] = self.collection.json()
        return d

    def from_json(self, s):
        self.__dict__.update(json.loads(s))


def search_databases(
    dbs,
    *,
    ksize=None,
    scaled=None,  # min scaled
    keyword=None,
    moltype=None,
):
    for db in dbs.values():
        match = False
        if ksize and ksize in db.ksizes:
            match = True
        if scaled and db.scaled >= scaled:
            match = True
        if moltype and moltype in db.moltypes:
            match = True
        if keyword:
            if keyword in db.title or keyword in db.description:
                match = True

        if match:
            yield db
