
def roman_value(s):
    if not isinstance(s, str):
        raise ValueError('Argument must be a string')
    if s == '':
        return 0
    if len(s) == 1:
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        elif s == 'M':
            return 1000
        raise ValueError('Argument must be a valid roman numeral character')
    first_value = roman_value(s[0])
    second_value = roman_value(s[1])
    if (second_value > first_value):
        return second_value - first_value + roman_value(s[2:])
    return first_value + roman_value(s[1:])
