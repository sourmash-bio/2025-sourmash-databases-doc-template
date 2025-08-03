# Collection: {{ coll.title }}

{{ coll.description }}

Links:

{% for (descr, url) in coll.links -%}
* [{{ descr }}]({{ url }})
{%- endfor %}

## Database files:

Files:
{% for db in coll.sketches %}
{% for dbfile in db.files -%}
   * {{ dbfile.fmt }}: [{{ dbfile.basename }}]({{ dbfile.download_url }}) - {{ dbfile.description }} - {{ dbfile.moltype }}, k={{ dbfile.ksize }}, scaled={{ dbfile.scaled }}
{% endfor %}
{% endfor %}

## Taxonomy files:

{% for tax in coll.taxonomies -%}
* [{{ tax.description }}]({{ tax.download_url }})
{% endfor %}

## Advanced

### Download commands

```shell
{% for db in coll.sketches -%}
{% for dbfile in db.files -%}
# download {{dbfile.basename}}
curl -O --no-clobber {{ dbfile.download_url }}
{% endfor -%}
{% endfor -%}
```
