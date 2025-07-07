# Describe a recursive function for converting a string of digits into the
# integer it represents. For example, 13531 represents the integer 13,531.

def convert_int(str):
    if len(str) == 1:
        return int(str[0])

    return 10 * convert_int(str[:-1]) + int(str[-1])
