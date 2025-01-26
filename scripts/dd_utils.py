# add:
# release date
# version
# smash database release
# sourmash version
# add num species, num genomes?
# taxonomy type (normal, lins, ??)
# "learn" sha256? or calc once & store? detect changes?

class Taxonomy:
    def __init__(self, *, short, title, description, source, lineage_file):
        self.short = str(short)
        self.title = str(title)
        self.description = str(description)
        self.source = str(source)
        self.lineage_file = lineage_file

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

        self._validate()

    def _validate(self):
        assert set(self.sources).issubset({"ncbi", "gtdb", "atb"}), self.sources
        assert self.category in ("bac+arc", "euk", "viruses"), self.category

        for x in self.links:
            assert x.startswith("http://") or x.startswith("https://"), x

        for t in self.taxonomies:
            assert isinstance(t, Taxonomy)

    def json(self):
        d = dict(self.__dict__)
        d['taxonomies'] = [ t.json() for t in self.taxonomies ]
        return d

    def from_json(self, s):
        self.__dict__.update(json.loads(s))

class SketchDatabases:
    def __init__(
        self,
        *,
        short,
        collection,
        ksizes,
        moltypes,
        scaled,
        fmt,
        index_type,
        download_url,
        filename,
    ):
        assert isinstance(collection, GenomeCollection)
        self.collection = collection

        self.short = str(short)
        self.ksizes = list(map(int, ksizes))
        self.moltypes = list(moltypes)
        self.scaled = int(scaled)
        self.fmt = fmt
        self.index_type = index_type
        self.filename = str(filename)
        self.download_url = str(download_url)

        self._validate()

    def _validate(self):
        assert min(self.ksizes) >= 4, self.ksizes
        assert max(self.ksizes) <= 101, self.ksizes

        for moltype in self.moltypes:
            assert moltype in {
                "DNA",
                "protein",
                "skipm1n3",
                "skipm2n3",
                "dayhoff",
                "hp",
            }, (moltype, self.moltypes)

        assert self.scaled >= 1, self.scaled
        assert self.scaled <= 1e9, self.scaled

        assert self.fmt in {"zip", "tar.gz"}
        assert self.index_type in {"zipfile", "lca.json", "rocksdb"}

    def __str__(self):
        return f"{self.title}"

    def json(self):
        d = dict(self.__dict__)
        d['collection'] = self.collection.json()
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
