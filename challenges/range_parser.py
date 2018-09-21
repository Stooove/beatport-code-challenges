"""
Implement a function that returns an inclusive list of numbers
from a Python slice style string with 1 <= N <= 10.

    '1'      # returns [1]
    ':7'     # returns [1, 2, 3, 4, 5, 6, 7]
    '8:'     # returns [8, 9, 10]
    '2:5'    # returns [2, 3, 4, 5]
    'a:b'    # returns 'Range values must be integers!'
    '1:2:3'  # returns 'Only two values allowed!'
    ':'      # what should this return?
    '7:5'    # what should this return?
    ''       # what should this return?

"""


def range_parser(s):
    """Use Python slice style string (s) to return inclusive list of numbers or
    error message as string."""
    error, error_msg, colon_count, first_num, last_num = s_transform(s)
    if error:
        return error_msg  # return as string
    else:
        return slicer(s, colon_count, first_num, last_num)  # return as list


def s_transform(s):
    """Using provided string (s), check if it generates an error when transformed for slice().
    Return: error (T/F), error_msg (string), colon_count (int), potential_first_num(int), potential_last_num(int)."""
    no_error = ''
    error1 = 'Range values must be integers!'
    error2 = 'Only two values allowed!'
    if ':' in s:
        if s.count(':') != 1:
            return True, error2, s.count(':'), 0, 0
        else:
            potential_first_num = '1' if s[:s.find(':')] == '' else s[:s.find(':')]
            potential_last_num = '10' if s[s.find(':') + 1:] == '' else s[s.find(':') + 1:]
            return (True, error1, 1, 0, 0) if not (can_be_int(potential_first_num)) and not \
                (can_be_int(potential_last_num)) else (False, no_error, 1, int(potential_first_num), int(potential_last_num))
    else:
        return (True, error1, 0, 0, 0) if not can_be_int(s) else (False, no_error, 0, 0, 0)


def slicer(s, colon_count, first_num, last_num):
    """Given string s such that int(s) is true, colon_count is 0 or 1, slice inclusive list by first_num (int), last_num (int),
    return sliced list."""
    inclusive_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return inclusive_list[slice(int(s) - 1, 11, 11)] if colon_count == 0 else inclusive_list[slice(first_num - 1, last_num)]


def can_be_int(s):
    """Return True if given string (s) can be an int, otherwise False."""
    try:
        int(s)
        return True
    except ValueError:
        return False