#! /usr/bin/env python
import sys
from optparse import OptionParser, make_option
from bank import *


def main():
    def checkRequiredArguments(options, parser):
        error_arguments = []
        if options.type is None:
            error_arguments.append('Type must be specified.')

        if options.bank is None:
            error_arguments.append('Bank name must be specified.')

        if options.file is None:
            error_arguments.append('File must be specified.')

        if error_arguments:
            parser.error(
                'Missing REQUIRED parameters: ' + str(error_arguments)
            )

    option_list = [
        make_option(
            "-f", "--file", type="string", dest="file",
            help=("xls file with alla transactions from the bank")
        ),
        make_option(
            "-b", "--bank", type="choice", dest="bank",
            choices=['ABN', ], help=("Bank name to choose from")
        ),
        make_option(
            "-t", "--type", type="choice", dest="type", default=1,
            choices=['0', '1'], help=(
                "type of calculation. it should be 1 for "
                "income or 0 for expenses"
            )
        ),
        make_option(
            "-p", "--pattern", type="string", dest="pattern",
            help="pattern to search in the description of every transaction"
        ),
    ]

    parser = OptionParser(
        "usage: %prog [options])",
        option_list=option_list,
        version="%prog 0.1"
    )

    (options, args) = parser.parse_args()

    checkRequiredArguments(options, parser)

    bank = globals()[options.bank](options.file)
    bank.get_amount(int(options.type), options.pattern)

if __name__ == '__main__':
    sys.exit(main())
