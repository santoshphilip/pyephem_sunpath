"""play with decorators"""

import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def suffix(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result + " suffix"
        return modified_result
    return wrapper

def greet(name, title="Mr"):
    """just a greet"""
    return "Hello! {}.{}".format(title, name)


@suffix
def sgreet(name, title="Mr"):
    """greet with a suffix"""
    return greet(name, title)

@uppercase
def ugreet(name, title="Mr"):
    """Upper case greet"""
    return greet(name, title)

@suffix
@uppercase
def sugreet(name, title="Mr"):
    """this is a suffix and upper greet"""
    return greet(name, title)

@uppercase
@suffix
def usgreet(name, title="Mr"):
    """greet with upper suffix"""
    return greet(name, title)

print greet("George")
print '-' * 5
print greet('James', 'Mr')
print greet.__name__
print greet.__doc__
print '-' * 5
print sgreet('James', 'Mr')
print sgreet.__name__
print sgreet.__doc__
print '-' * 5
print ugreet('James', 'Mr')
print ugreet.__name__
print ugreet.__doc__
print '-' * 5
print sugreet('James', 'Mr')
print sugreet.__name__
print sugreet.__doc__
print '-' * 5
print usgreet('James', 'Mr')
print usgreet.__name__
print usgreet.__doc__
print '-' * 5



