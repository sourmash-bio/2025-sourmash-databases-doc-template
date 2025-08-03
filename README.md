# 2025-sourmash-databases-doc-template

Run `make`. Then look at [outputs/md](outputs/md) to see output markdown.

## Previewing formatting with mkdocs

Run `mkdocs serve` to see the generated files.

## Updating sourmash database list

Copy all the files in `outputs/md/` into the sourmash repo under `doc/databases-md/`.

## Adding databases

Edit [scripts/databases.py](scripts/databases.py) to add databases.

You'll also need to:
* add the new db to 'collections' list at top of `scripts/make-md.py`.
* update `mkdocs.yml` if you want to preview the new db;
* update `doc/databases.md` in sourmash to include a direct link to the generated file.

## Validating database links

Run `outputs/scripts/check-urls.py` to check that all the database and
taxonomy URLs are valid.

## Notes on database naming conventions:

* all NCBI databases will be date-stamped
* all GTDB databases will be version-stamped
