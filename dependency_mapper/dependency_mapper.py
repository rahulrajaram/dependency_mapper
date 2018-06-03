import subprocess
import sys

import six
import tabulate
import termcolor

from dependency_mapper import arguments_context


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

        if (
            not args_context.show_all
            and args_context.highlight
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


def output(args_context):
    output = tabulate.tabulate(header_list(args_context), tablefmt='grid')

    for header in args_context.highlight:
        colored_version = termcolor.colored(header, 'red', attrs=['bold', 'underline'])
        print(colored_version)
        output = output.replace(header, colored_version)

    print(output)


def describe_headers():
    output(arguments_context.create())
