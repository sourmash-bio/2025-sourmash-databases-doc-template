#! /usr/bin/env python
import sys
import argparse
import os
import re
import shutil
import traceback
import json


jinja_env = None
from jinja2 import Environment, FileSystemLoader


def render_template(filename, *, values={}, outpath=None):
    try:
        template = jinja_env.get_template(filename)
    except:
        traceback.print_exc()
        print(' in template:', filename)
        return False

    try:
        rendered = template.render(values)
    except:
        traceback.print_exc()
        print(' in file:', filename)
        return False

    with open(outpath, 'wt') as fp:
        fp.write(rendered)


def main(argv=sys.argv[1:]):
    global jinja_env
    assert jinja_env is None

    p = argparse.ArgumentParser()
    p.add_argument('databases_json')
    args = p.parse_args(argv)

    with open(args.databases_json, 'rt') as fp:
        databases = json.load(fp)
        print(databases)

    # Load jinja templates from disk (templates folder)
    jinja_env = Environment(
        loader=FileSystemLoader('templates')
    )

    render_template('test.md', values=databases, outpath='out.md')


if __name__ == '__main__':
    main()
