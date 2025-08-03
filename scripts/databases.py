# globally accessible
BASE_URL = "https://farm.cse.ucdavis.edu/~ctbrown/sourmash-db.new"

# file path on farm, our local HPC :)
FILE_PATH = "/group/ctbrowngrp5/sourmash-db.new"

from dd_utils import Taxonomy, GenomeCollection, SketchDatabases, Params

### GTDB rs220

gtdb220_tax = Taxonomy(
    short="gtdb220",
    title="GTDB RS220 taxonomy",
    description="GTDB taxonomy for RS220.",
    source="gtdb",
    lineage_file="gtdb-rs220/gtdb-rs220.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

gtdb220 = GenomeCollection(
    short="gtdb220",
    title="GTDB RS220",
    description="Bacterial and Archaeal genomes from GTDB RS220.",
    category="bac+arc",
    sources=["gtdb", "ncbi"],
    links=[
        (
            "Announcement",
            "https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r09-rs220/595",
        )
    ],
    taxonomies=[gtdb220_tax],
)

gtdb220_entire_dna = SketchDatabases(
    short="gtdb220_entire_dna",
    collection=gtdb220,
    description="all GTDB genomes.",
    params=[
        Params(ksize=21, moltype="DNA", scaled=1000, size_gb=17),
        Params(ksize=31, moltype="DNA", scaled=1000, size_gb=17),
        Params(ksize=51, moltype="DNA", scaled=1000, size_gb=17),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs220/gtdb-rs220-k{ksize}.dna.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

gtdb220_reps_dna = SketchDatabases(
    short="gtdb220_reps_dna",
    collection=gtdb220,
    description="all GTDB species representative genomes.",
    params=[
        Params(ksize=21, moltype="DNA", scaled=1000, size_gb=2.8),
        Params(ksize=31, moltype="DNA", scaled=1000, size_gb=2.8),
        Params(ksize=51, moltype="DNA", scaled=1000, size_gb=2.8),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs220/gtdb-reps-rs220-k{ksize}.dna.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

### GTDB rs226

gtdb226_tax = Taxonomy(
    short="gtdb226",
    title="GTDB RS226 taxonomy",
    description="GTDB taxonomy for RS226.",
    source="gtdb",
    lineage_file="gtdb-rs226/gtdb-rs226.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

gtdb226 = GenomeCollection(
    short="gtdb226",
    title="GTDB RS226",
    description="Bacterial and Archaeal genomes from GTDB RS226.",
    category="bac+arc",
    sources=["gtdb", "ncbi"],
    links=[
        (
            "Announcement",
            "https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r10-rs226/724",
        )
    ],
    taxonomies=[gtdb226_tax],
)

gtdb226_entire_dna = SketchDatabases(
    short="gtdb226_entire_dna",
    collection=gtdb226,
    description="all GTDB genomes.",
    params=[
        Params(ksize=21, moltype="DNA", scaled=1000, size_gb=21),
        Params(ksize=31, moltype="DNA", scaled=1000, size_gb=21),
        Params(ksize=51, moltype="DNA", scaled=1000, size_gb=21),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs226/gtdb-rs226-k{ksize}.dna.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

gtdb226_reps_dna = SketchDatabases(
    short="gtdb226_reps_dna",
    collection=gtdb226,
    description="all GTDB species representative genomes.",
    params=[
        Params(ksize=21, moltype="DNA", scaled=1000, size_gb=21),
        Params(ksize=31, moltype="DNA", scaled=1000, size_gb=21),
        Params(ksize=51, moltype="DNA", scaled=1000, size_gb=21),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs226/gtdb-reps-rs226-k{ksize}.dna.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

### NCBI viruses

ncbi_virus_tax_2025_01 = Taxonomy(
    short="ncbi_virus_tax_2025_01",
    title="NCBI viral taxonomy",
    description="NCBI taxonomy for viruses as of January 2025.",
    source="ncbi",
    lineage_file="ncbi-viruses-2025.01/ncbi-viruses.2025.01.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_viruses_2025_01 = GenomeCollection(
    short="ncbi_viruses_2025_01",
    title="NCBI Viruses (Jan 2025)",
    description="All viruses from NCBI (NCBI:txid10239) as of January 2025.",
    category="viruses",
    sources=["ncbi"],
    links=[
        (
            "NCBI Taxonomy",
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=10239&lvl=3&lin=f&keep=1&srchmode=1&unlock",
        )
    ],
    taxonomies=[ncbi_virus_tax_2025_01],
)

ncbi_viruses_2025_01_dna = SketchDatabases(
    short="ncbi_viruses_2025_01_dna",
    description="all viral genomes.",
    collection=ncbi_viruses_2025_01,
    params=[
        Params(ksize=21, moltype="DNA", scaled=50, size_gb=1.4),
        Params(ksize=31, moltype="DNA", scaled=50, size_gb=1.4),
        Params(ksize=24, moltype="skip_m2n3", scaled=50, size_gb=2.7),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="ncbi-viruses-2025.01/ncbi-viruses-2025.01.{moltype_l}.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

### NCBI Eukaryotes

ncbi_euk_tax_2025_01 = Taxonomy(
    short="ncbi_euk_tax_2025_01",
    title="NCBI eukaryotic taxonomy",
    description="NCBI taxonomy for eukaryotes (NCBI:txid2759) as of January 2025.",
    source="ncbi",
    lineage_file="genbank-euks-2025.01/ncbi-eukaryotes.2025.01.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euks_2025_01 = GenomeCollection(
    short="ncbi_euks_2025_01",
    title="NCBI Eukaryotes (Jan 2025)",
    description="All eukaryotic reference genomes from NCBI (NCBI:txid2759) as of January 2025.",
    category="euk",
    sources=["ncbi"],
    links=[
        (
            "NCBI Taxonomy",
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=2759&lvl=3&lin=f&keep=1&srchmode=1&unlock",
        )
    ],
    taxonomies=[ncbi_euk_tax_2025_01],
)

ncbi_euks_2025_01_vert = SketchDatabases(
    short="ncbi_euks_vertebrates",
    description="vertebrate reference genomes (NCBI:txid7742)",
    collection=ncbi_euks_2025_01,
    params=[
        Params(ksize=51, moltype="DNA", scaled=10000, size_gb=4),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2025.01/ncbi-euks-vertebrates-2025.01.dna.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euk_2025_01_bilateria = SketchDatabases(
    short="ncbi_euks_bilateria_no_vert",
    description="bilateria minus the vertebrates",
    collection=ncbi_euks_2025_01,
    params=[
        Params(ksize=51, moltype="DNA", scaled=10000, size_gb=1.7),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2025.01/ncbi-euks-bilateria-minus-vertebrates-2025.01.dna.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euk_2025_01_plants = SketchDatabases(
    short="ncbi_euks_plants",
    description="plant reference genomes (NCBI:txid33090)",
    collection=ncbi_euks_2025_01,
    params=[
        Params(ksize=51, moltype="DNA", scaled=10000, size_gb=1.3),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2025.01/ncbi-euks-plants-2025.01.dna.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euks_2025_01_fungi = SketchDatabases(
    short="ncbi_euks_fungi",
    description="fungal reference genomes (NCBI:txid4751)",
    collection=ncbi_euks_2025_01,
    params=[
        Params(ksize=51, moltype="DNA", scaled=10000, size_gb=0.2),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2025.01/ncbi-euks-fungi-2025.01.dna.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euks_2025_01_metazoa = SketchDatabases(
    short="ncbi_euks_metazoa",
    description="metazoan reference genomes minus the bilateria",
    collection=ncbi_euks_2025_01,
    params=[
        Params(ksize=51, moltype="DNA", scaled=10000, size_gb=0.1),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2025.01/ncbi-euks-metazoa-minus-bilateria-2025.01.dna.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euks_2025_01_other = SketchDatabases(
    short="ncbi_euks_other",
    description="remaining eukaryotes (not plants, fungi, or metazoa)",
    collection=ncbi_euks_2025_01,
    params=[
        Params(ksize=51, moltype="DNA", scaled=10000, size_gb=0.1),
    ],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2025.01/ncbi-euks-other-2025.01.dna.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)
