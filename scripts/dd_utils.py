# add:
# release date
# version
class Database:
    def __init__(self, *,
                 title,
                 description,
                 sources,
                 ksizes,
                 moltype,
                 scaled,
                 fmt,
                 index_type,
                 download_url,
                 sha256):
        self.title = str(title)
        self.description = str(description)
        self.sources = list(sources)

        self.ksizes = list(map(int, ksizes))
        self.moltype = str(moltype)
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

        assert self.moltype in {'DNA', 'protein', 'skipm1n3', 'skipm2n3',
                                'dayhoff', 'hp'}, self.moltype
        
        assert self.scaled >= 1, self.sscaled
        assert self.scaled <= 1e9, self.scaled

        assert self.fmt in {'zip', 'tar.gz'}
        assert self.index_type in {'zipfile', 'lca.json', 'rocksdb'}
