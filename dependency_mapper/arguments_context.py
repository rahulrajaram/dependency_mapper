import argparse


class FormatterClass(argparse.RawDescriptionHelpFormatter):
    def __init__(
            self,
            prog,
            indent_increment=2,
            max_help_position=30,
            width=100
    ):
        super(FormatterClass, self).__init__(
                prog,
                indent_increment=indent_increment,
                max_help_position=max_help_position,
                width=width
        )

    def add_usage(self, usage, actions, groups, prefix=None):
        pass


def create():
    parser = argparse.ArgumentParser(
    description="""Simple tool to draw the header-file dependency map of your C/C++ project.

    Usage:
        cd <path/to/project/source>
        describe_headers [optional arguments]
""",
        formatter_class=FormatterClass
    )
    parser.add_argument(
        '-hl',
        '--highlight',
        default=[],
        help='(sub)strings to highlight; use this to highlight specific file/header file names',
        nargs='*'
    )
    parser.add_argument(
        '-p',
        '--path',
        default='.',
        help='directory in which the source files whose dependencies to map are located; defaults to the present working directory'
    )
    parser.add_argument(
        '-c',
        '--curtail',
        action='store_true',
        default=False,
        help='optionally curtail search output to only those rows containing highlighted text (works with --highlight/-hl); defaults to false'
    )
    parser.add_argument(
        '-s',
        '--parse-system-headers',
        action='store_true',
        default=False,
        help='additionally search for directives specified using system-headers delimiters, "<...>", to parse header files; defaults to false'
    )

    return parser.parse_args()
