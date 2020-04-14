import re


def int_to_roman(input_num):
    if check_minus_input(input_num) and check_zero_input(input_num):
        roman_dict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_dict = sorted(roman_dict.items(), key=lambda x: x[1], reverse=True)

        rst = ''
        for (char, i) in roman_dict:
            count = input_num // i
            input_num = input_num % i
            rst += count * char

        rst = rst\
            .replace('DCCCC', 'CM')\
            .replace('CCCC', 'CD')\
            .replace('LXXXX', 'XC')\
            .replace('XXXX', 'XL')\
            .replace('VIIII', 'IX')\
            .replace('IIII', 'IV')
        return rst


def roman_to_int(input_num):

    if input_num.islower():
        input_num = input_num.upper()

    roman_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    num = 0
    list_s = re.findall('CM|CD|XC|XL|IX|IV|I|V|X|L|C|D|M', input_num)

    for input_num in list_s:
        num += roman_dict[input_num]
    return num


def convert_str_to_integer(input_num):
    if not isinstance(int(input_num), int):
        raise ValueError("Input number is not an integer. Please input an positive integer!")
    else:
        return int(input_num)


def check_minus_input(input_num):
    if input_num < 0:
        raise ValueError("Input number is minus. Please input an positive integer!")
    else:
        return True


def check_zero_input(input_num):
    if 0 == input_num:
        raise ValueError("Input number is zero. Please input an positive integer!")
    else:
        return True


def check_int_input(input_num):
    if not input_num.isalpha():
        raise ValueError("The input is arabic number. Please input a roman number.")


"""sorted(iterable, *, key=None, reverse=False)
    Return a new sorted list from the items in iterable.
    Has two optional arguments which must be specified as keyword arguments.
    key specifies a function of one argument that is used to extract a comparison key 
    from each element in iterable (for example, key=str.lower). 
    The default value is None (compare the elements directly).
    reverse is a boolean value. If set to True, then the list elements are sorted as if 
    each comparison were reversed.
"""
"""re.findall(pattern, string, flags=0)
        Return all non-overlapping matches of pattern in string, as a list of strings. 
        The string is scanned left-to-right, and matches are returned in the order found. 
        If one or more groups are present in the pattern, return a list of groups; 
        this will be a list of tuples if the pattern has more than one group. 
        Empty matches are included in the result.
"""
"""
    Floor Division(//)
    Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
"""