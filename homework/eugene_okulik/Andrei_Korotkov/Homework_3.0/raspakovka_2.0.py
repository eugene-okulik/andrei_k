
print('=' * 36)
print('Задание: ', 1, sep='№')
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country, sep='|')

print('=' * 36)
print('Задание: ', 2, sep='№')

chislo_1 = ('Результат работы программы: 15')
string_index_1 = chislo_1.index(':') + 2
srez_1 = chislo_1[string_index_1:]
print(int(srez_1) + 10)

chislo_2 = ('Результат работы программы: 66')
string_index_2 = chislo_2.index(':') + 2
srez_2 = chislo_2[string_index_2:]
print(int(srez_2) + 10)

chislo_3 = ('Результат работы программы: 899')
string_index_3 = chislo_3.index(':') + 2
srez_3 = chislo_3[string_index_3:]
print(int(srez_3) + 10)

print('=' * 43)
print('Задание: ', 3, sep='№')
students = ['Ivanov', 'Petrov', 'Sidorov']
# students = ', '.join(students)
# print(students)
subjects = ['math', 'biology', 'geography']
# subjects = ', '.join(subjects)
# print(subjects)
students, subjects = ', '.join(students), ', '.join(subjects)
print('Students', students, 'study these subjects:', subjects)
print('=' * 43)
