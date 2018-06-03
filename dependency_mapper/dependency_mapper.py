import subprocess
import sys

import argparse

import six
import tabulate
import termcolor


class FormatterClass(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        pass


def grep_output():
    (stdout, stderr) = subprocess.Popen(['grep', '-r', "^#include \"*\""], stdout=subprocess.PIPE).communicate()

    string_output = stdout if sys.version_info < (3, 0) else stdout.decode()
    return string_output.strip().split('\n')


def header_dict(args_context):
    _header_dict = dict()
    for line in grep_output():
        file_name, header_name = [component.strip().strip('"') for component in line.split(':#include')]
        if not file_name or not header_name:
            continue
        if not args_context.show_all:
            if (
                args_context.highlight
                and not (
                    [f for f in args_context.highlight if file_name in f or f in file_name]
                    or [f for f in args_context.highlight if header_name in f or f in header_name]
                )
            ):
                continue

        if _header_dict.get(file_name):
            _header_dict[file_name].append(header_name)
        else:
            _header_dict[file_name] = [header_name]
    return _header_dict


def header_list(args_context):
    _file_to_headers_mappings_list = list()
    for key, value in six.iteritems(header_dict(args_context)):
        _file_to_headers_mappings_list.append([key, '\n'.join(value)])
    _file_to_headers_mappings_list.sort(key=lambda mapping: mapping[0])

    return _file_to_headers_mappings_list


def arguments_context():
    parser = argparse.ArgumentParser(
    description="""Simple tool to draw the header-file dependency map of your C/C++ project.',

    Usage:
        cd <path/to/project/source>
        describe_headers
""",
        formatter_class=FormatterClass
    )
    parser.add_argument(
        '-hl',
        '--highlight',
        default=[],
        help='specify header file names to highlight',
        nargs='*'
    )
    parser.add_argument(
        '-a',
        '--show-all',
        action='store_true',
        default=False,
        help='show all responses even if header file names are specified to be highlighted'
    )

    return parser.parse_args()


def output(args_context):
    output = tabulate.tabulate(header_list(args_context), tablefmt='grid')

    for header in args_context.highlight:
        colored_version = termcolor.colored(header, 'red', attrs=['bold', 'underline'])
        print(colored_version)
        output = output.replace(header, colored_version)

    print(output)


def describe_headers():
    output(arguments_context())
