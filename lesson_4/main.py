
a = "test"

print(type(list))

class My:
    pass

print(type(My))

def my_func():
    pass

a = type('MyClass', (), {'attr1': 1,
                         'attr2': 2,
                         'func_1': my_func})



class MyClass1:
    attr1 = 1
    attr2 = 2

    def func_1(self):
        pass
print(a)
print(dir(a))
print(a.attr1)
print(a.attr2)
a_obj = a()
a.func_1()