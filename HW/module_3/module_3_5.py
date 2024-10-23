def get_multiplied_digits(number):
    if len(str(number)) == 1:
        return number
    else:
        str_number = str(number)
        first = int(str_number[:1])
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
