
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

print(f'{GREEN}=' * 36)
print(f'{GREEN}Задание: №2 {RESET}', sep='№')
print(f'{GREEN}=' * 36)

my_range = range(1, 101)
for number in my_range:
    if number % 3 == 0 and number % 5 == 0:
        print(f'{RED}Fuzz{BLUE}Buzz{RESET}')
    elif number % 3 == 0:
        print(f'{BLUE}Fuzz{RESET}')
    elif number % 5 == 0:
        print(f'{RED}Buzz{RESET}')
    else:
        print(f'{YELLOW}{number}')

print(f'{YELLOW}=' * 36)
