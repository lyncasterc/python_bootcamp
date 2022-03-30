def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Bye!")
    return wrapper

# The above function takes another function, x, as an arg, then defines yet another function,y, inside of it, which calls the arg function x, and then returns that function y.



def greet():
    print("my name is job.")


greet = be_polite(greet)
greet()

# the variable greet is set to the top outer function with the greet function passed in.
# The variable greet now becomes a function, the wrapper function. This is a decorator

@be_polite
def rage():
    print("I HATE YOU!")

# the syntax above functions in the exact same way as the previous example with the greet variable.



# decorators can also take arguments

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def gureet(name):
    
    return f"hi {name} "

print(gureet("Dave"))

