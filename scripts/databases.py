BASE_URL = "https://farm.cse.ucdavis.edu/~ctbrown/sourmash-db"
FILE_PATH = "@CTB"

from dd_utils import Taxonomy, GenomeCollection, SketchDatabases, Params


gtdb220_tax = Taxonomy(
    short="gtdb220",
    title="GTDB RS220 taxonomy",
    description="GTDB taxonomy for RS220",
    source="gtdb",
    lineage_file="gtdb-rs220.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

gtdb220 = GenomeCollection(
    short="gtdb220",
    title="GTDB RS220",
    description="All Bacteria and Archaea from GTDB RS220",
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
    params=[Params(ksize=21, moltype="DNA", scaled=1000),
            Params(ksize=31, moltype="DNA", scaled=1000),
            Params(ksize=51, moltype="DNA", scaled=1000)],
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs220/gtdb-rs220-k{ksize}.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

###

ncbi_virus_tax = Taxonomy(
    short="ncbi_virus_tax",
    title="NCBI viral taxonomy",
    description="NCBI taxonomy for viruses",
    source="ncbi",
    lineage_file="ncbi-viruses.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_viruses_2025_01 = GenomeCollection(
    short="ncbi_viruses_2025_01",
    title="NCBI Viruses",
    description="All viruses from NCBI (NCBI:txid10239)",
    category="viruses",
    sources=["ncbi"],
    links=[
        (
            "NCBI Taxonomy",
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=10239&lvl=3&lin=f&keep=1&srchmode=1&unlock",
        )
    ],
    taxonomies=[ncbi_virus_tax],
)

ncbi_viruses_2025_01_dna = SketchDatabases(
    short="ncbi_viruses_2025_01_dna",
    collection=ncbi_viruses_2025_01,
    params=[Params(ksize=21, moltype="DNA", scaled=50),
            Params(ksize=31, moltype="DNA", scaled=50),
            Params(ksize=24, moltype="skip_m2n3", scaled=50)],
    fmt="zip",
    index_type="zipfile",
    filename="ncbi-viruses-2025.01/ncbi-viruses.{moltype_l}.k={ksize}.scaled={scaled}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

###

ncbi_euk_tax = Taxonomy(
    short="ncbi_euk_tax",
    title="NCBI eukaryotic taxonomy",
    description="NCBI taxonomy for eukaryotes (NCBI:txid2759)",
    source="ncbi",
    lineage_file="ncbi-eukaryotes.lineages.csv",
    download_url=f"{BASE_URL}/{{filename}}",
)

ncbi_euks_2025_01 = GenomeCollection(
    short="ncbi_euks_2025_01",
    title="NCBI Eukaryotes",
    description="All eukaryotes from NCBI (NCBI:txid2759)",
    category="viruses",
    sources=["ncbi"],
    links=[
        (
            "NCBI Taxonomy",
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=2759&lvl=3&lin=f&keep=1&srchmode=1&unlock",
        )
    ],
    taxonomies=[ncbi_euk_tax],
)

ncbi_euks_2025_01_vert = SketchDatabases(
    short="ncbi_euks_vertebrates",
    collection=ncbi_euks_2025_01,
    params=[Params(ksize=51, moltype="DNA", scaled=10000),],
    fmt="zip",
    index_type="zipfile",
    filename="genbank-euks-2024.01/vertebrates.k={ksize}.sig.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)

