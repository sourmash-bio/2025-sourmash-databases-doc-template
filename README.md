# 2025-sourmash-databases-doc-template

Edit [scripts/databases.py](scripts/databases.py) to add databases.

Also add to 'collections' list at top of `scripts/make-md.py`.

Run `snakemake -j 1`. Then look at [outputs/md](outputs/md) to see output.

## Notes

* all NCBI databases will be date-stamped
* all GTDB databases will be version-stamped
