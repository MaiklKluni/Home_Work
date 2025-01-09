from pprint import pprint


def custom_write(file_name, strings):
    slovar = {}
    with open(file_name, 'a+', encoding='utf-8') as file:
        i = 0
        for st in strings:
            i += 1
            key = (i, file.tell())
            slovar[key] = st
            file.write(st + '\n')
    return slovar


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
