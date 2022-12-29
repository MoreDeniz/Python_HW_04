# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


def encode(equation: str) -> dict:
    equation = ' ' + equation 
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
        .replace('*x ', '*x**1 ').split()[:-2]
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[0] = int(i[0])
    return dict_equation

def decode(equation: dict) -> str:
    new_equation = []   # пустой список
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' ' + ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ')\
        .replace('*x**0', '').replace(' 1*x', ' x').replace('-1*x', '-x').replace('x**1', 'x')
    return new_equation[1:]

def addition(first_eq: dict, second_eq: dict):
    final_eq = {}
    final_eq.update(first_eq)
    final_eq.update(second_eq)
    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0)
    return final_eq


with open("file_1.txt") as file:
    equa_1 = file.read()
    print(equa_1)

with open("file_2.txt") as file:
    equa_2 = file.read()
    print(equa_2)

equation1 = encode(equa_1)
equation2 = encode(equa_2)

print(equation1)
print(equation2)

print(decode(equation1))
print(decode(equation2))

sum_polynomials = decode(addition(equation1, equation2))
print(sum_polynomials)

with open('file_3.txt', 'w') as data:
    data.write(sum_polynomials)