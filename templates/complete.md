# Collection: {{ db.collection.title }} - {{ db.collection.description }}

Links:
{% for (descr, url) in db.collection.links -%}
* [{{ descr }}]({{ url }})
{%- endfor %}

## Database files:

Files:
{% for dbfile in db.files -%}
   * {{ dbfile.fmt }}: [{{ dbfile.basename }}]({{ dbfile.download_url }}) - {{ dbfile.moltype }}, k={{ dbfile.ksize }}, scaled={{ dbfile.scaled }}
{% endfor %}

## Taxonomy files:

{% for tax in db.collection.taxonomies -%}
* [{{ tax.description }}]({{ tax.download_url }})
{% endfor %}
