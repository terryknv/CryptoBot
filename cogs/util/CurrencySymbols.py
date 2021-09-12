class CurrencySymbols:
    curr_list: {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'INR': '₹',
        'AUD': '$',
        'CAD': '$',
        'SGD': '$',
        'JPY': '¥',
        'CNY': '¥'
        }

#CurrencySymbols.curr_list['USD']

    @staticmethod
    def is_valid_curr(currency):
        if currency in curr_list:
            return True
        else:
            return False
