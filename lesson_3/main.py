def func(name='name', age=20):
    pass


func(name='new_name', age=18)


my_new_var = 10


#Curying example


def a(a_arg):
    print(a_arg)

    def b(b_arg):
        print(b_arg)

        def c(c_arg):
            print(c_arg)
            print('The end of function tree')

        return c

    return b

#Decorators basics

def func1(func):
    print('Hello i am func1')
    print('Function started')
    func()
    print('Function ended')


#func1(random_generator)

def decorator(func):

    def wrapper(range_start, range_end):
        result = []
        for iteration_num, _ in enumerate(range(100)):
            number = func(range_start, range_end)
            result.append(number)

        return result

    return wrapper


@decorator
def random_generator(range_start, range_end):
    import random
    return random.randint(range_start, range_end)

#with @ syntax
result = random_generator(100, 200)

#without @ syntax
#result = decorator(random_generator)(100, 200)

print(result)


