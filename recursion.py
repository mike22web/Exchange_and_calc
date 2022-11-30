import random
def counter_f(func):
    #counter = 0
    def wrapper(*args, **kwargs):
        counter += 1
        func(*args, **kwargs)
    counter = 0
    return wrapper






s = []
@counter_f
def digit(n):
    s.append(random.randint(1, 100))
    if n == 1:
        return s, sum(s)
    return digit(n-1)

