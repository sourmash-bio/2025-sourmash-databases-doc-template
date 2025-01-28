all: Snakefile
	snakemake --delete-all-output
	snakemake -p

format:
	black scripts
