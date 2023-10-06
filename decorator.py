import math
import time
def timer(func):
    def inner(*args, **kwargs): #*args is used for more argument
        print('Time Started')
        start = time.time()
        # print(func)
        func(*args, **kwargs)
        print('Time Ended')
        end = time.time()
        print(f'total time taken {end - start}')
    return inner

# timer()

@timer
def factorial(n):
    print('Factorial starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

# factorial(5)
factorial(n = 1500)

