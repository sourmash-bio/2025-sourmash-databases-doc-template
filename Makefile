.PHONY: build format update_sourmash

all: Snakefile build preview

build:
	snakemake --delete-all-output
	snakemake -p -j 1

preview: build
	rm -fr preview/generated
	mkdir -p preview/generated/
	cp outputs/md/*.md preview/generated/

update_ctb_sourmash: build
	cp -r outputs/md/ ~/dev/sourmash/doc/databases-md/

format:
	black scripts
