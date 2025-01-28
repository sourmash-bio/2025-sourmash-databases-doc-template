# Collection: {{ gtdb220_entire_dna.collection.title }} - {{ gtdb220_entire_dna.collection.description }}

Links:
{% for (descr, url) in gtdb220_entire_dna.collection.links -%}
* [{{ descr }}]({{ url }})
{%- endfor %}

## Database files:

Files:
{% for dbfile in gtdb220_entire_dna.files -%}
   * {{ dbfile.fmt }}: [{{ dbfile.basename }}]({{ dbfile.download_url }}) - {{ dbfile.moltype }}, k={{ dbfile.ksize }}, scaled={{ dbfile.scaled }}
{% endfor %}

## Taxonomy files:

{% for tax in gtdb220_entire_dna.collection.taxonomies -%}
* [{{ tax.description }}]({{ tax.download_url }})
{% endfor %}
