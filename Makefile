all: Snakefile
	snakemake -p

format:
	black scripts
