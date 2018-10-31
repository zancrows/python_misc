# coding: utf-8
# python 3.7.0 x86_64

from copy import copy, deepcopy

class Singleton(type):   
    _instance = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Foo(metaclass=Singleton):
    pass

    
class Bar(Foo):
    pass

def main():
    foo = Foo()
    foo_2 = Foo()
    
    bar = Bar()
    bar_2 = Bar()
    
    print("foo:")
    print(foo == foo_2)
    print(foo is foo_2)
    
    print("bar:")
    print(bar == bar_2)
    print(bar is bar_2)
    
if __name__ == "__main__":
    main()