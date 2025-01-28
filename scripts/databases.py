BASE_URL = "https://farm.cse.ucdavis.edu/~ctbrown/sourmash-db"
FILE_PATH = "@CTB"

from dd_utils import Taxonomy, GenomeCollection, SketchDatabases


gtdb220_tax = Taxonomy(
    short="gtdb220",
    title="GTDB RS220 taxonomy",
    description="All Bacteria and Archaea from GTDB RS220",
    source='gtdb',
    lineage_file='gtdbrs220_taxonomy_file',
    download_url=f"{BASE_URL}/{{filename}}",
)

gtdb220 = GenomeCollection(
    short="gtdb220",
    title="GTDB RS220",
    description="All Bacteria and Archaea from GTDB RS220",
    category="bac+arc",
    sources=["gtdb", "ncbi"],
    links=[("Announcement", "https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r09-rs220/595")],
    taxonomies = [gtdb220_tax],
)

gtdb220_entire_dna = SketchDatabases(
    short='gtdb220_entire_dna',
    collection=gtdb220,
    moltypes=["DNA"],
    ksizes=[21, 31, 51],
    scaled=1000,
    fmt="zip",
    index_type="zipfile",
    filename="gtdb-rs220/gtdb-rs220-k{ksize}.zip",
    download_url=f"{BASE_URL}/{{filename}}",
)
