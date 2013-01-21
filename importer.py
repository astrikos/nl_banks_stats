#! /usr/bin/env python
import sys
import pickle
import json


def importer(import_file):
    if import_file:
        file2import = import_file
    else:
        file2import = 'income'

    with open(file2import, 'r') as f:
        new_data = f.read()
        new_data = json.loads(new_data)

    try:
        with open('incomes.pkl', 'rb') as f:
            incomes_list = pickle.load(f)
    except IOError:
        print 'no initial income pickle file'
        incomes_list = []

    for v in new_data.values():
        incomes_list.extend(v)
    f = open('incomes.pkl', 'wb')
    pickle.dump(incomes_list, f)
    f.close()


if __name__ == '__main__':
    import_file = ''
    if len(sys.argv) > 1:
        import_file = sys.argv[1]

    importer(import_file)
