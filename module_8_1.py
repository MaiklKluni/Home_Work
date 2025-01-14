def add_everything_up(a, b):
    try:
        c = a + b

    except TypeError:
        if isinstance(a, str):
            c = a + str(b)
        else:
            c = str(a) + b
    finally:
        return c

if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))