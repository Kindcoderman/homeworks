calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_ = (len(string),) + (string.upper(),) + (string.lower(),)
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [name.lower() for name in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)