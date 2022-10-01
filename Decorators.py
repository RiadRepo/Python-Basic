#
# def outerClass (massege):
#     print('hello outer is working!!');
#     def inneClass ():
#         print("Hello im inner class")
#         print(f'inner class text is working {massege}')
#     return inneClass
#
# f = outerClass("oohooo!")
# f()

#decorators
def decorator(original_fun):
    print("first part working")
    def wrapper():
        print(f'wrapper function executed before {original_fun.__name__}')
        if 10>5:
            print("its true!!")
        return original_fun()
    return wrapper

@decorator
def print_something():
    print('all done')

# over = decorator(print_something)
# over()

print_something()
#non keyword argument f(1,2,3)
#keyword argument f(a=1,b=2,c=3)

def decorator_2(original_func):
    print("its working first")
    def warraper (*args ,**kwargs ):
        print(f'warraper before execute {original_func.__name__}' )
        if 12>10:
            print("all right")
        return original_func(*args,**kwargs)
    return warraper

@decorator_2
def print_something2(args1,args2):
    print(f'here first {args1} and second {args2}')

print_something2(1,2)



