import re


def validar_ncm(ncm):
    pattern = r'^\d{8}$'
    if not isinstance(ncm, str):
        return False
    if not re.match(pattern, ncm):
        return False
    return True


def remove_digito(string: str) -> str:
    """ Remove digit and return the numeric part from a string """
    def _return_num(string_slice: str):
        if string_slice.isnumeric():
            return string_slice
        else:
            return ''
    return ''.join([_return_num(_str) for _str in string])


def remove_digito_to_float(string: str) -> str:
    """ Remove digit and return the numeric part from a string and returns a float"""
    def _return_num(string_slice: str):
        if string_slice.isnumeric():
            return string_slice
        elif string_slice == '.':
            return string_slice
        else:
            return ''
    return ''.join([_return_num(_str) for _str in string])