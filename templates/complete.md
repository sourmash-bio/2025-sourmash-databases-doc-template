# Database: {{ gtdb220_entire_dna.short  }}

* {{ gtdb220_entire_dna.short }}
* {{ gtdb220_entire_dna.moltypes }}
* {{ gtdb220_entire_dna.ksizes }}
* {{ gtdb220_entire_dna.scaled }}
* {{ gtdb220_entire_dna.fmt }}

Ksizes:
  {% for ksize in gtdb220_entire_dna.ksizes %}
     {{ ksize }}
  {% endfor %}

Moltypes:
  {% for moltype in gtdb220_entire_dna.moltypes %}
     {{ moltype }}
  {% endfor %}

## Collection: {{ gtdb220_entire_dna.collection.short }}

* {{ gtdb220_entire_dna.collection.short }}

## Taxonomies

{% for tax in gtdb220_entire_dna.collection.taxonomies %}

### {{ tax.title }}
* {{ tax.description }}
* {{ tax.lineage_file }}

{% endfor %}
