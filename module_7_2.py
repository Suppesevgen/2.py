from pprint import pprint

name = 'test.txt'
file = open(name, 'w', encoding='utf-8')
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    strings_positions = {}
    with open(name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings):
            start_byte = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, start_byte)] = string
    return strings_positions

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)