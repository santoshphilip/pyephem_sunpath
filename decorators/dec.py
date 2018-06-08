"""play with decorators"""

# def null_decorator(func):
#     print func
#     return func
#
# def greet():
#     return "Hello!"
#
# greet = null_decorator(greet)
#
# @null_decorator
# def greet():
#     return "Hello!"
#

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return "Hello!"

uppergreet = greet()




