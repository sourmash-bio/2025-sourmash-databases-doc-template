from collections import namedtuple

TEMPLATES, = glob_wildcards('templates/{filename}.md')

Templates_To_Output = namedtuple("Templates_To_Output",
                                 ['dbname', 'template_name', 'output_md'])

templates = [
    Templates_To_Output('gtdb220',
                        'complete',
                        'outputs/md/gtdb220.md'),
    Templates_To_Output('ncbi_viruses_2025_01',
                        'complete',
                        'outputs/md/ncbi_viruses_2025_01.md'),
    Templates_To_Output('ncbi_euks_2025_01',
                        'complete',
                        'outputs/md/ncbi_euks_2025_01.md'),
]

def get_template_path(w):
    print('gtp', w)
    for t in templates:
        if t.output_md == f'outputs/md/{w.db}.md':
            x = f'templates/{t.template_name}.md'
            print('get_template_path', t, x)
            return x

def get_template_name(w):
    for t in templates:
        if t.output_md == f'outputs/md/{w.db}.md':
            x = f'{t.template_name}.md'
            print('get_template_name', t, x)
            return x

### rules

rule default:
    input:
        [ t.output_md for t in templates ],


rule make_db_descr:
    input:
        script='scripts/make-list.py',
    output:
        pickle='outputs/collections.pickle',
    shell: """
        {input.script} --save-pickle {output.pickle}
    """


rule make_gtdb:
    input:
        script='scripts/make-md.py',
        pickle='outputs/collections.pickle',
        template_path=get_template_path,
    output:
        "outputs/md/{db}.md",
    params:
        template=get_template_name,
    shell: """
        {input.script} {input.pickle} {params.template} \
            --set-collection {wildcards.db} -o {output}
    """
