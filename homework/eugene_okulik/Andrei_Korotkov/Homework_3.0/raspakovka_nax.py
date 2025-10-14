
print('=' * 36)
print('Задание: ', 1, sep='№')
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country, sep='|')

print('=' * 36)
print('Задание: ', 2, sep='№')

chislo_1 = ('Результат работы программы:', 16)
print(chislo_1[-1] + 10)

chislo_2 = ('Результат работы программы:', 656)
print(chislo_2[-1] + 10)

chislo_3 = ('Результат работы программы:', 5)
print(chislo_3[-1] + 10)

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