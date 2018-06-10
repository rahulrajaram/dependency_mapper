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
        help='optionally curtail output if requested to highlight certain text using --highlight; defaults to false'
    )
    parser.add_argument(
        '-s',
        '--parse-system-headers',
        action='store_true',
        default=False,
        help='use system-headers delimiters, "<...>", to parse header files; defaults to false'
    )

    return parser.parse_args()
