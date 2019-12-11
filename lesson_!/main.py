
list_1 = [1, 2, 'asd', 3, 4, 5]

list_2 = list([1, 2, 3, 4])

list_1[0] = 'zero'

print(list_1[0])

# tuple_1 = (1, )
# tuple_1[0] = 10
# print(tuple_1[0])


dict_1 = {
    'one': 1,
    'two': 2,
    (1, 2): 3,
    'three': [1, 2, 3]

}



print(dict_1.get('three', 10))
print(dict_1[(1, 2)])


print(set([1, 2, 2, 2, 3]))


#user_string = input('ENTer smth')

# if user_string:
#     print(user_string[::-1])
# elif True:
#     pass
# elif True:
#     pass
# else:
#     print('String is empty')


# number = int(input('ENTer number'))
#
# if number > 100:
#     print('more than 100')
# else:
#     print('IDK')


# result = 'more than 100' if number > 100 else None
# print(result)
#
# i = 0
# while True:
#     a = str(input('ENther smth'))


list2 = range(100)
len_of_list = 9
i = 0
while i < len_of_list:
    print(list2[i])
    i += 1


dict_1 = {
    'one': 1,
    'two': 2,
    (1, 2): 3,
    'three': [1, 2, 3]

}

a = 10
b = 20

a = (1, 2, 3)

c, d, e = a

print(c, d, e)

print('*' * 10)
for k in dict_1.items():
    print(k[0], k[1])

try:
    b = 1 + 'a'
    a = 1 / 0
except:
    a = None
else:
    print('Exception wasnt caught')
finally:
    print('Exception block ended')

raise Exception('error messagel')











