all: Snakefile
	snakemake --delete-all-output
	snakemake -p -j 1

format:
	black scripts
