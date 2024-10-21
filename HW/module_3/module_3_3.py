# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('abc')
print_params(5, 'x')
print_params('qwerty', False, 77)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = [False, 6, 'seven']
values_dict = {'a': 'text', 'b': False, 'c': 4}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [True, 'text']
print_params(*values_list_2, 42)