
list_of_names = ['john', 'helen', 'nencie', 'jack']

def making_upper(string):
    return string.upper()

#1
results = []
for name in list_of_names:
    results.append(making_upper(name))
print(results)
#2
print([making_upper(name) for name in list_of_names])

#3
print(list(map(making_upper, list_of_names)))

mr = map(lambda x, y: (x.upper(), y.upper()), list_of_names, list_of_names)
print(list(mr))


def func(extra_value, **kwargs):
    for k, v in kwargs.items():
        if v == extra_value:
            kwargs.pop(k)
            break
    return kwargs


extra_value = '12312qeqwrwqqwqwr'
kwargs = {
    'sum': 12,
    'id': 134,
    'comment': 'user_comment',
    'token': '12312qeqwrwqqwqwr'
}

d1 = dict(filter(lambda kv: kv[1] != extra_value, kwargs.items()))
d2 = func(extra_value, **kwargs)


print(d1)
print(d2)