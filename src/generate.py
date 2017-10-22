import os, sys
import json
import argparse
from jinja2 import Template

BASE_DIR = os.path.dirname(__file__)


def get_tests():
    tests = {}
    resource_dir = "{}/resources".format(BASE_DIR)
    for file_ in os.listdir(resource_dir):
        if file_.endswith("resource.json"):
            content = os.path.join(resource_dir, file_)
            with open(content) as fp:
                tests[file_.split(".")[0]] = json.load(fp)
    return tests


def main(show_answer):
    tests = get_tests()
    template_source = "{}/template/index.html".format(BASE_DIR)
    with open(template_source) as fp:
        template = fp.read()
        for name, content in tests.iteritems():
            result_html = "{}/done/{}.html".format(BASE_DIR, name)
            Template(template).stream(test=content, show_correct_answer=show_answer).dump(result_html)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test generator')
    parser.add_argument('--with_answer',  dest='with_answer', action='store_true', help='Generate test with correct answer')
    args = parser.parse_args()

    main(args.with_answer)
