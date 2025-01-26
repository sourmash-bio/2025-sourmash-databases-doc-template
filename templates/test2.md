Download URL {{ gtdb220_dna.k51.download_url }}

Filename: {{ gtdb220_dna.k51.filename }}

Title: {{ gtdb220_dna.collection.title }}

{% for tax in gtdb220_dna.collection.taxonomies %}
{{ tax.title }}
* {{ tax.description }}
* {{ tax.lineage_file }}

{% endfor %}
