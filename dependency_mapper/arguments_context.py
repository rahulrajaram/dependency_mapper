import argparse


class FormatterClass(argparse.RawDescriptionHelpFormatter):
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
        help='specify header file names to highlight',
        nargs='*'
    )
    parser.add_argument(
        '-a',
        '--show-all',
        action='store_true',
        default=False,
        help='show all results even if header file names are specified to be highlighted thorugh --highlight'
    )
    parser.add_argument(
        '-p',
        '--path',
        help='directory in which the source files whose dependencies to map are located; defaults to the present working directory'
    )

    return parser.parse_args()
