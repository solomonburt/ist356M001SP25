def clean_currency(value:str) -> float:
    '''
    This function will take a string value and remove the dollar sign and commas
    and return a float value.
    '''
    return float(value.replace(',', '').replace('$', ''))


# tests
assert clean_currency('$1,000.00') == 1000.00
assert clean_currency('$1,000') == 1000.00
assert clean_currency('1,000') == 1000.00
assert clean_currency('$1000') == 1000.00