TEMPLATES, = glob_wildcards('templates/{filename}.md')

rule default:
    input:
        expand('outputs/md/{name}.md', name=TEMPLATES)


rule make_db_json:
    input:
        script='scripts/make-list.py',
    output:
        json='outputs/databases.pickle',
    shell: """
        {input.script} --save-pickle {output.json}
    """


rule make_md_from_template:
    input:
        template='templates/{name}.md',
        script='scripts/make-md.py',
        json='outputs/databases.pickle',
    output:
        md='outputs/md/{name}.md',
    shell: """
        {input.script} {input.json} {wildcards.name}.md -o {output.md}
    """
