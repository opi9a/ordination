import sys

def ordinate(num, include_digit=True):
    '''Converts an input integer to a string representation
    of the corresponding ordinal indicator.  Eg

        1   -->   '1st'
        2   -->   '2nd'
        11  -->  '11th'
        12  -->  '12th'
        21  -->  '21st'
        22  -->  '22nd'
        100 --> '100th'

    Optionally drop the digit by passing include_digit=False
    to return 'st', 'nd' etc
    '''

    if not isinstance(num, int):
        raise TypeError("ordinate() requires an integer input")
        return 1

    last_digit = num % 10

    prefix = num if include_digit else ""

    if last_digit == 1:
        if num % 100 != 11:
            return prefix + 'st'

    if last_digit == 2:
        if num % 100 != 12:
            return prefix + 'nd'

    if last_digit == 3:
        if num % 100 != 13:
            return prefix + 'rd'

    return prefix + 'th'


def main_function():

    try:
        num = int(sys.argv[1])
    except:
        print("Need an integer\n")
        return

    include_digit = True

    if len(sys.argv) == 3:
        if sys.argv[2] in ['-n', '--no-digit']:
            include_digit = False
        else:
            print("Don't recognise ", sys.argv[2])
            print("Only valid flag is -n or --no-digit")
            return

    print(ordinate(num, include_digit))

if __name__=="__main__": main_function()
