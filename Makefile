.PHONY: build format

all: Snakefile build preview

build:
	snakemake --delete-all-output
	snakemake -p -j 1

preview: build
	rm -fr preview/generated
	mkdir -p preview/generated/
	cp outputs/md/*.md preview/generated/
	#mkdocs build

format:
	black scripts
