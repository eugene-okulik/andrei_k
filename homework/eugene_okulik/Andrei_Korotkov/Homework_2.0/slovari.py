
my_dict = {
    'tuple': (21, 55, 'AQA', 'Python', 66.6),
    'list': [22, 32.4, 54, 'SQL', False],
    'dict':
        {'key_1': '1',
         'key_2': '6',
         'key_3': '20.5',
         'key_4': 'Git_hub',
         'key_5': 'True'
         },
    'set': {45, 67, False, 'Books', 32.5}
}

print(my_dict['tuple'])
print(my_dict['tuple'][-1])

print(my_dict['list'])
my_dict['list'].append('Homework')
my_dict['list'].pop(1)
print(my_dict['list'])

print(my_dict['dict'])
my_dict['dict'][('i am a tuple',)] = "Slovar"
my_dict['dict'].pop('key_2')
print(my_dict['dict'])

print(my_dict['set'])
my_dict['set'].add('Testers')
my_dict['set'].remove(32.5)
print(my_dict['set'])
