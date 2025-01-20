#! /usr/bin/env python
import sys
import argparse

from glom import glom
from dd_utils import Database, search_databases
import json

gtdb_entire_k31 = Database(
    short='gtdb_entire_k31',
    title='GTDB: entire database, RS220',
    description='All Bacteria and Archaea from GTDB rs220',
    sources=['gtdb', 'ncbi'],
    moltypes=['DNA'],
    ksizes=[31],
    scaled=1000,
    fmt='zip',
    index_type='zipfile',
    download_url='',
    sha256='')

databases = dict(gtdb_entire_k31=gtdb_entire_k31)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--keyword', type=str)
    p.add_argument('-k', '--ksize', type=int)
    p.add_argument('-s', '--scaled', type=float)
    p.add_argument('-o', '--output-json')
    args = p.parse_args()

    scaled = args.scaled
    if scaled is not None:
        scaled = int(scaled)

    results = []
    for db in search_databases(databases,
                               keyword=args.keyword,
                               ksize=args.ksize,
                               scaled=scaled):
        results.append((db.short, db.json()))

    if not results:
        results = [ (db.short, db.json()) for db in databases.values() ]

    results = dict(results)

    print(f'got {len(results)} dbs.')

    if args.output_json:
        with open(args.output_json, 'wt') as fp:
            json.dump(results, fp, indent=4)


if __name__ == '__main__':
    sys.exit(main())

