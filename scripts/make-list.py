#! /usr/bin/env python
import sys
import argparse
import pickle

from glom import glom
from dd_utils import Taxonomy, GenomeCollection, SketchDatabases, search_databases
from databases import *
import json


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
