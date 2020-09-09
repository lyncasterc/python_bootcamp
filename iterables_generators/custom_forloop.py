def my_for(iterable,func):
    iterator = iter(iterable)

    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)


def square(x):
    print(x*x)
    
my_for([1,2,3,4],square)

