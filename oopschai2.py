#decoraters ( a toll were all function go from it )

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, country="India")

#-----------------------------------------------
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))      
print(add_numbers(5, 10, 15, 20)) 
#-----------------------------------------------
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}  time ")
        return result
    return wrapper
@timer
def example (n):
    time.sleep(n)
example(2)
#---------------------------------------------------
#
def debug(func):
    def wrapper (*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@debug
def hell():
    print("hello world ")

hell()

@debug
def greet(name , greeting = "kya hua bai"):
    print (f"{name} , {greeting}")

greet("Nehal", "hello Bhia")