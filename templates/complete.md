# Database: {{ gtdb220_entire_dna.short  }}

* {{ gtdb220_entire_dna.short }}
* {{ gtdb220_entire_dna.moltypes }}
* {{ gtdb220_entire_dna.ksizes }}
* {{ gtdb220_entire_dna.scaled }}
* {{ gtdb220_entire_dna.fmt }}

{% for dbfile in gtdb220_entire_dna.files %}
   {{ dbfile.fmt }}: [{{ dbfile.basename }}]({{ dbfile.download_url }}) - k={{ dbfile.ksize }}, moltype={{ dbfile.moltype }}, scaled={{ dbfile.scaled }}
{% endfor %}

## Collection: {{ gtdb220_entire_dna.collection.short }}

* {{ gtdb220_entire_dna.collection.short }}

## Taxonomies

{% for tax in gtdb220_entire_dna.collection.taxonomies %}

### {{ tax.title }}
* {{ tax.description }}
* {{ tax.lineage_file }}

{% endfor %}
