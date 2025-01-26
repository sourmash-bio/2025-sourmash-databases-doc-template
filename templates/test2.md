Download URL {{ gtdb220_entire_dna.k51.download_url }}

Filename: {{ gtdb220_entire_dna.k51.filename }}

Title: {{ gtdb220_entire_dna.collection.title }}

{% for tax in gtdb220_entire_dna.collection.taxonomies %}
{{ tax.title }}
* {{ tax.description }}
* {{ tax.lineage_file }}

{% endfor %}
