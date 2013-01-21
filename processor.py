#! /usr/bin/env python
import pickle
import re
from datetime import datetime


date_pattern = re.compile('^.*?\/Date\((.+?)000\)\s*\/.*?$', re.I)


def processor():
    try:
        with open('incomes.pkl', 'rb') as f:
            incomes_list = pickle.load(f)
    except IOError:
        print 'no initial income pickle file'
        return

    total = 0
    for income in incomes_list:
        if 'ripe ncc' in income['FriendlyName']:
            timestamp = int(date_pattern.match(income['Date']).group(1))
            timestr = datetime.fromtimestamp(timestamp).strftime(
                "%Y-%m-%d %H:%M:%S")
            print timestr, income['FriendlyName'], income['Value']
            total += income['Value']

    print 'Total income: #%d' % total

if __name__ == '__main__':
    processor()
