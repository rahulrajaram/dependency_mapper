import subprocess
import sys

import argparse

import six
from tabulate import tabulate


class FormatterClass(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        pass


def grep_output():
    (stdout, stderr) = subprocess.Popen(['grep', '-r', "^#include \"*\""], stdout=subprocess.PIPE).communicate()

    string_output = stdout if sys.version_info < (3, 0) else stdout.decode()
    return string_output.strip().split('\n')


def header_dict():
    _header_dict = dict()
    for line in grep_output():
        file_name, header_name = [component.strip().strip('"') for component in line.split(':#include')]
        if not file_name or not header_name:
            continue

        if _header_dict.get(file_name):
            _header_dict[file_name].append(header_name)
        else:
            _header_dict[file_name] = [header_name]
    return _header_dict


def header_list():
    _file_to_headers_mappings_list = list()
    for key, value in six.iteritems(header_dict()):
        _file_to_headers_mappings_list.append([key, '\n'.join(value)])
    _file_to_headers_mappings_list.sort(key=lambda mapping: mapping[0])

    return _file_to_headers_mappings_list


def help_text_interception():
    parser = argparse.ArgumentParser(
    description="""Simple tool to draw the header-file dependency map of your C/C++ project.',

    Usage:
        cd <path/to/project/source>
        describe_headers
""",
        formatter_class=FormatterClass
    )
    parser.parse_args()


def describe_headers():
    help_text_interception()    

    print(tabulate(header_list(), tablefmt='grid'))
