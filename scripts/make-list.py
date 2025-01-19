#! /usr/bin/env python
from dd_utils import Database
import json

gtdb_entire_k31 = Database(
    title='GTDB: entire database, RS220',
    description='All Bacteria and Archaea from GTDB rs220',
    sources=['gtdb', 'ncbi'],
    moltype='DNA',
    ksizes=[31],
    scaled=1000,
    fmt='zip',
    index_type='zipfile',
    download_url='',
    sha256='')

x = json.dumps(dict(gtdb_entire_k31=gtdb_entire_k31.__dict__))
print(x)
