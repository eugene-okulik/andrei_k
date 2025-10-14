
print('=' * 36)
print('Задание: ', 1, sep='№')
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country, sep='|')

print('=' * 36)
print('Задание: ', 2, sep='№')

chislo_1 = ('Результат работы программы:', 15)
raspokovka_1 = f"{chislo_1[0]} {chislo_1[1]}"
search_1 = int(raspokovka_1.split()[-1])
print(search_1 + 10)

chislo_2 = ('Результат работы программы:', 343333)
raspokovka_2 = f"{chislo_2[0]} {chislo_2[1]}"
search_2 = int(raspokovka_2.split()[-1])
print(search_2 + 10)

chislo_3 = ('Результат работы программы:', 545)
raspokovka_3 = f"{chislo_3[0]} {chislo_3[1]}"
search_3 = int(raspokovka_3.split()[-1])
print(search_3 + 10)

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
