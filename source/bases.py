#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    if(base == 2):
        sum = 0
        for i in range(len(digits) - 1, -1, -1):
            # Multiply current digit by 2 to its correct power.
            # The power starts at 0 and increments by 1 every for loop run
            sum += int(digits[i]) * (2 ** (len(digits) - i - 1))
        return sum
    elif base == 16:
        sum = 0
        # Go From Last digit to First digit
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is a letter, get its correct value; A=10 B=11 C=12...
            curDigit = (ord(digits[i].upper()) - 55) if digits[i].isalpha() else digits[i]
            # Multiply current digit by 16 to its correct power.
            # The power starts at 0 and increments by 1 every for loop run
            sum += int(curDigit) * (16 ** (len(digits) - i - 1))
        return sum
    elif base >= 2 or base <= 36:
        sum = 0
        # Go From Last digit to First digit
        for i in range(0, len(digits)):
            # If the current digit is a letter, get its correct value; A=10 B=11 C=12...
            curDigit = (ord(digits[i].upper()) - 55) if digits[i].isalpha() else digits[i]
            # Multiply current digit by the base to its correct power.
            # The power starts at 0 and increments by 1 every for loop run
            sum += int(curDigit) * (base ** (len(digits) - i - 1))
        return sum


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    number = int(number)
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    if base == 2:
        binList = []
        if number < 2:
            # 1 and 0's
            return str(number)
        else:
            binList.extend((encode(number / 2, 2), encode(number % 2, 2)))
        return "".join(binList)
    elif base == 16:
        hexList = []
        if number < 10:
            return str(number)
        elif number < 16:
            return chr(number + 55).lower()
        else:
            hexList.extend((encode(number / 16, 16), encode(number % 16, 16)))
        return "".join(hexList)
    else:
        resultList = []
        if number < 10 and number < base:
            return str(number)
        elif number >= 10 and number < base:
            return chr(number + 55).lower()
        else:
            resultList.extend((encode(number / base, base), encode(number % base, base)))
        return "".join(resultList)

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base{} is {} in base{}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
