
def sum_func(my_arg1, *args, name='MyName',**kwargs):
    result = 0
    print(my_arg1)
    for i in args:
        result += i
    return result


a = [1, 2, 3, 4]

print(sum_func())
#The same



