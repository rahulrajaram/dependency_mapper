import subprocess
import sys

import six
import tabulate
import termcolor

from dependency_mapper import arguments_context


def grep(search_candidates, parse_system_headers=False):
    directive_patterns = ['^#include ".*"']
    if parse_system_headers:
        directive_patterns.append("^#include <.*>")

    grep_args = [
        'grep',
        "-EorI",
        "{}".format('|'.join(directive_patterns)),
        '--exclude-dir=.git',
    ] + search_candidates

    (stdout, stderr) = subprocess.Popen(grep_args, stdout=subprocess.PIPE).communicate()

    string_output = stdout if sys.version_info < (3, 0) else stdout.decode()
    return string_output.strip().split('\n')


def header_dict(args_context):
    _header_dict = dict()
    for line in grep(args_context.paths, args_context.parse_system_headers):
        if not line.strip():
            continue
        file_name, header_name = [
            component.strip().strip('"').strip('<').strip('>') for component in line.split(':#include')
        ]

        if not file_name or not header_name:
            continue

        def matched(name):
            return [f for f in args_context.highlight if name in f or f in name]

        if (
            args_context.curtail
            and not matched(file_name)
            and not matched(header_name)
        ):
            continue

        _header_dict.setdefault(file_name, []).append(header_name)
    return _header_dict


def header_list(args_context):
    _file_to_headers_mappings_list = list()
    for key, value in six.iteritems(header_dict(args_context)):
        _file_to_headers_mappings_list.append([key, '\n'.join(sorted(value))])
    _file_to_headers_mappings_list.sort(key=lambda mapping: mapping[0])

    return _file_to_headers_mappings_list


def output(args_context):
    output = tabulate.tabulate(header_list(args_context), tablefmt='grid')
    for header in args_context.highlight:
        colored_version = termcolor.colored(header, 'red', attrs=['bold', 'underline'])
        output = output.replace(header, colored_version)
    print(output)


def describe_headers():
    output(arguments_context.create())
