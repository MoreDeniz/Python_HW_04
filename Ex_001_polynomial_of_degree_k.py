import random

my_dict = {}
number = int(input('Введите целое положительное число: '))
for n in range(0, number+1):
    my_dict[n] = random.randint(0, 100)
    if my_dict[n] == 0:
        my_dict[n] = random.randint(1, 100)

print(my_dict)

my_string = []
new_str = []
for key, item in my_dict.items():
    if key == 0:
        my_string.append('{} = 0'.format(item))
    elif key == 1:
        my_string.append('{} * x'.format(item))
    elif item == 0:
        my_string.append('')
    else:
        my_string.append('{} * x**{}'.format(item, key))

new_str = new_str.append(my_string)
my_string.reverse()  # Переворачиваем список
print(' + '.join(my_string))
