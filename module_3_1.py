def count_calls(num):
    global calls
    calls += num


def string_info(st=''):
    count_calls(1)
    _kort = (len(st), st.upper(), st.lower())
    return _kort


def is_contains(st='', sp=[]):
    count_calls(1)
    if st.lower() in (item.lower() for item in sp):
        return True
    else:
        return False


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)