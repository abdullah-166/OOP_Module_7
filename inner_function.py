def double():
    print('starting the double')
    def inner_function():
        print('inside the door')
        return 500
    return inner_function

# print(double())
# print(double()())

def do_something(work):
    print('work started')
    # print(work)
    work()
    print('work ended')

# do_something(5)
# do_something('i am busy now')

def coding():
    print('coding in python')
do_something(coding)

def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping)