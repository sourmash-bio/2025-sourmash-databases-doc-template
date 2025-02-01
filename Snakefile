TEMPLATES, = glob_wildcards('templates/{filename}.md')

rule default:
    input:
        "outputs/md/gtdb_entire_dna.md",


rule make_db_descr:
    input:
        script='scripts/make-list.py',
    output:
        pickle='outputs/databases.pickle',
    shell: """
        {input.script} --save-pickle {output.pickle}
    """


rule make_md_from_template:
    input:
        template='templates/{name}.md',
        script='scripts/make-md.py',
        pickle='outputs/databases.pickle',
    output:
        md='outputs/md/{name}.md',
    shell: """
        {input.script} {input.pickle} {wildcards.name}.md -o {output.md}
    """

rule make_gtdb:
    input:
        script='scripts/make-md.py',
        pickle='outputs/databases.pickle',
        template_path="templates/complete.md"
    output:
        "outputs/md/gtdb_entire_dna.md",
    params:
        db="gtdb220_entire_dna",
        template="complete.md",
    shell: """
        {input.script} {input.pickle} {params.template} --db {params.db} -o {output}
    """
