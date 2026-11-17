#cython syntax experiment
#see how it uses python syntax, except for the variables which are much closer to C

def say_something():
    cdef int a = 3
    cdef int b = 4

    print(a+b)

    return "Hey it's me Goku!"

def goku_count():
    cdef int a = 0
    for i in range(100000):
        a += 1
    return a