from pandas import ExcelFile


class Bank(object):

    def __init__(self, transactions_file):
        self.transactions_file = transactions_file
        self.import_data(transactions_file)

    def import_data(self, transactions_file):
        pass


class ABN(Bank):
    def import_data(self, transactions_file):
        xls = ExcelFile(transactions_file)
        self.data = xls.parse('Sheet0', index_col=3, na_values=['NA'])

    def get_amount(self, transaction_type, pattern):
        if transaction_type:
            t_slice = self.data[[d > 0 for d in self.data['amount']]]
        else:
            t_slice = self.data[[d < 0 for d in self.data['amount']]]

        final_slice = t_slice
        if pattern:
            final_slice = t_slice[
                [pattern.lower() in d.lower() for d in t_slice['description']]
            ]

        amount_series = final_slice['amount']
        if transaction_type:
            word = 'income'
        else:
            word = 'expenses'
        print 'Total amount of %s is: %dE' % (
            word,
            sum([d for d in amount_series])
        )
