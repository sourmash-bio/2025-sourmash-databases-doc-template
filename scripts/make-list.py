#! /usr/bin/env python
import sys
import argparse
import pickle

from glom import glom
from dd_utils import Taxonomy, GenomeCollection, SketchDatabases, search_databases
import json

BASE_URL = "https://farm.cse.ucdavis.edu/~ctbrown/sourmash-db"

FILE_PATH = "@CTB"


gtdb220_tax = Taxonomy(
    short="gtdb220",
    title="GTDB RS220 taxonomy",
    description="All Bacteria and Archaea from GTDB RS220",
    source='gtdb',
    lineage_file='gtdbrs220_taxonomy_file',
    # @CTB download_url
)

gtdb220 = GenomeCollection(
    short="gtdb220",
    title="GTDB RS220",
    description="All Bacteria and Archaea from GTDB RS220",
    category="bac+arc",
    sources=["gtdb", "ncbi"],
    links=["http://link_to_gtdb"],
    taxonomies = [gtdb220_tax],
)

gtdb220_entire_dna = SketchDatabases(
    short='gtdb220_dna',
    collection=gtdb220,
    moltypes=["DNA"],
    ksizes=[21, 31, 51],
    scaled=1000,
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs220/gtdb-rs220-k{ksize}.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)


databases = [
    gtdb220_entire_dna,
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--keyword", type=str)
    p.add_argument("-k", "--ksize", type=int)
    p.add_argument("-s", "--scaled", type=float)
    p.add_argument("--output-json")
    p.add_argument("-o", "--save-pickle")
    args = p.parse_args()

    scaled = args.scaled
    if scaled is not None:
        scaled = int(scaled)

    print(databases[0])

    if args.output_json:
        assert 0

    if args.save_pickle:
        with open(args.save_pickle, "wb") as fp:
            pickle.dump(databases, fp)


if __name__ == "__main__":
    sys.exit(main())
