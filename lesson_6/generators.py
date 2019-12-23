def counter(start, end):

    while start <= end:
        yield start

        start += 1
        print('I am gen func')

c = counter(0, 2)

def randomizer(steps):
    import random
    current_step = 0
    value = 0
    while current_step <= steps:
        value += random.random()
        current_step += 1
        yield value




# [x for x in range(100)]
#
# a = list((x for x in range(100)))
# print(a)

for i in randomizer(100):
    print(i)

