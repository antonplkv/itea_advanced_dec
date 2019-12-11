
class Singletone:

    _objects = None

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        if cls._objects:
            raise Exception('Object already exists')

        obj = super().__new__(cls, *args, **kwargs)
        cls._objects = obj
        return obj

obj_1 = Singletone()
print(obj_1)
obj_2 = Singletone()
print(obj_2)
