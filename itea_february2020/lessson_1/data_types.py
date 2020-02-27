string = "Hello"
int_var = 100
float_var = 100.5

list_var = [1, 2, 3, string, int_var, float_var, 100]

# new_tuple = tuple(list_var)
# print(type(new_tuple))
#
# new_list = list(new_tuple)
# print(type(new_list))


list_var[0] = [1, 2, 3]




dict_var = {
    'name': 'John',
    'surname': 'Lehnon',
    'birthday': 1999


}


print(dict_var.get('birthday'))

dict_var['birthday'] = 2000

print(dict_var['birthday'])
my_dict = dict(
    word1=100,
    key2='value2',

)



# my_dict.items()
#
#
# dict_1 = {
#     [1, 2]: 'list'
# }

# a = {'zxc', 'cxz', 'zxc'}
# print(a.add('qwe'))
# print(a)
#
# b = frozenset(a)
#
# print(b.add('zxc'))



# z = frozenset(('zxcz', ))
# print(z)


# temperature = 20
#
#
# if temperature > 15:
#     print("Worm")
# elif temperature > 20:
#     print("Hot")
#
# elif temperature < 0:
#     print("Cold")
#
# else:
#     print("IDK")


nullables = (0, '', (), [], [])

print(bool(0))
print(bool(''))
print(bool([]))
name = "Andrew"
surname = "Nickolson"
birthday = "20.07.1984"


if name != None and surname != None and birthday != None:
    print(name)

else:
    print("Nothing to show")


# if any([name, surname, birthday]):
#     pass
#
#
# temperature = 20
#
#
# result = "Hot" if temperature > 20 else None

temperature = 20

# if temperature > 10:
#     print("Warm")
# elif temperature > 15:
#     print("Hot")
# elif temperature > 19:
#     print("Very hot")


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)


# i = 0
# while i < 15:
#     i += 1
#     if i == 9:
#         continue
#     print(i)
#
#     j = 0
#
#     while j < 10:
#         print(f'j{j}')
#         j += 1
#         if j == 3:
#             break



# my_list = [1, 2, 3]
# for idx, elem in enumerate(my_list):
#     print(elem[0], elem[1])


try:
    b = None
except (TypeError, AttributeError) as error:
    print(error.args)
    print(error.kwargs)
    b = error
else:
    print("No exception was occured")
finally:
    print('Finaly Block')


print(b)


def sum_func(arg1, arg2):
    return sum([arg1, arg2]), 100

resutlt = sum_func


def func1(sum_f, x1, x2):
    return sum_f(x1, x2)

r = func1(sum_func, 100, 100 )
print(r)

def test_sum(arg1, *args):
    return sum(args) / len(args)

def test_kwargs(**kwargs):
    print(kwargs)

# values = [100, 100, 100]
# second_values = [200, 200, 200]
# print(test_sum())

dict_to_kwargs = {
    'arg1': 1,
    'arg2': 3,
    'arg4': 100
}
test_kwargs(**dict_to_kwargs)

