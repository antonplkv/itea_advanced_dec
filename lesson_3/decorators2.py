def decorator(num_of_repeats):

    def actual_decorator(func):

        def wrapper(range_start, range_end):
            result = []
            for i in range(num_of_repeats):
                result.append(func(range_start, range_end))

            return result
        return wrapper
    return actual_decorator


@decorator(30)
def random_generator(range_start, range_end):
    import random
    return random.randint(range_start, range_end)

result = random_generator(10, 20)
print(result)
