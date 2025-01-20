# add:
# release date
# version
# taxonomy
class Database:
    def __init__(self, *,
                 short,
                 title,
                 description,
                 sources,
                 ksizes,
                 moltypes,
                 scaled,
                 fmt,
                 index_type,
                 download_url,
                 sha256):
        self.short = str(short)
        self.title = str(title)
        self.description = str(description)
        self.sources = list(sources)

        self.ksizes = list(map(int, ksizes))
        self.moltypes = list(moltypes)
        self.scaled = int(scaled)
        self.fmt = fmt
        self.index_type = index_type
        self.download_url = str(download_url)
        self.sha256 = str(sha256)

        self._validate()

    def _validate(self):
        assert set(self.sources).issubset({ 'ncbi',
                                            'gtdb',
                                            'atb' }), self.sources

        assert min(self.ksizes) >= 4, self.ksizes
        assert max(self.ksizes) <= 101, self.ksizes

        for moltype in self.moltypes:
            assert moltype in {'DNA', 'protein', 'skipm1n3', 'skipm2n3',
                               'dayhoff', 'hp'}, (moltype, self.moltypes)
        
        assert self.scaled >= 1, self.scaled
        assert self.scaled <= 1e9, self.scaled

        assert self.fmt in {'zip', 'tar.gz'}
        assert self.index_type in {'zipfile', 'lca.json', 'rocksdb'}

    def __str__(self):
        return f"{self.title}"

    def json(self):
        return self.__dict__


def search_databases(dbs, *,
                     ksize=None,
                     scaled=None, # min scaled
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
