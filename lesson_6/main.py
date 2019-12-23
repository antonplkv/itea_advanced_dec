import random
class Randomizer:

    def __init__(self, steps):
        self._steps = steps
        self._current_step = 0
        self._value = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self._current_step <= self._steps:
            self._value += random.random()
            self._current_step += 1

        else:
            raise StopIteration()
        return self._value

# class MyIter:
#
#     def __init__(self, start, end):
#         self._starter = Starter(start, end)
#
#     def __iter__(self):
#         return self._starter.__iter__()



obj = Randomizer(1000)

for i in obj:
    print(i)

# obj_iter = iter(obj)
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))


for i in obj:
    print(i)