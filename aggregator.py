#! /usr/bin/env python
import sys
from optparse import OptionParser, make_option
import pandas as pd


def aggregator(type, pattern):
    xls = pd.ExcelFile('income_data.xls')
    data = xls.parse('Sheet0', index_col=3, na_values=['NA'])
    if type:
        type_slice = data[[d > 0 for d in data['amount']]]
    else:
        type_slice = data[[d < 0 for d in data['amount']]]

    final_slice = type_slice
    if pattern:
        final_slice = type_slice[
            [pattern.lower() in d.lower() for d in type_slice['description']]
        ]

    amount_series = final_slice['amount']
    if type:
        word = 'income'
    else:
        word = 'expenses'
    print 'Total amount of %s is: %dE' % (
        word,
        sum([d for d in amount_series])
    )


def main():
    option_list = [
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

    parser = OptionParser("usage: %prog [options])", option_list=option_list)

    (options, args) = parser.parse_args()

    if options.type is None:
        parser.error("type must be specified")
        return 1

    aggregator(int(options.type), options.pattern)

if __name__ == '__main__':
    sys.exit(main())
