# Database: {{ gtdb220_entire_dna.collection.title  }} - {{ gtdb220_entire_dna.collection.description }}

Files:
{% for dbfile in gtdb220_entire_dna.files %}
   * {{ dbfile.fmt }}: [{{ dbfile.basename }}]({{ dbfile.download_url }}) - {{ dbfile.moltype }}, k={{ dbfile.ksize }}, scaled={{ dbfile.scaled }}
{% endfor %}

## Collection: {{ gtdb220_entire_dna.collection.short }}

* {{ gtdb220_entire_dna.collection.short }}

## Taxonomies

{% for tax in gtdb220_entire_dna.collection.taxonomies %}

### {{ tax.title }}
* {{ tax.description }}
* {{ tax.lineage_file }}

{% endfor %}
