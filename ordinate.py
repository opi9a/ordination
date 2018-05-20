import sys

def ordinate(num):
    '''Converts an input integer to a string representation of the corresponding
    ordinal indicator.

    Eg
        1   : '1st'
        2   : '2nd'
        11  : '11th'
        100 : '100th'
    '''

    if not isinstance(num, int):
        raise TypeError("ordinate() requires an integer input")
        return 1

    last_digit = num % 10

    if last_digit == 1:
        if num % 100 != 11:
            return str(num) + 'st'

    if last_digit == 2:
        if num % 100 != 12:
            return str(num) + 'nd'

    if last_digit == 3:
        if num % 100 != 13:
            return str(num) + 'rd'

    return str(num) + 'th'


if __name__=="__main__":

    if len(sys.argv) != 2:
        print("Only one integer input please\n")

    else:
        print(ordinate(int(sys.argv[1])))
