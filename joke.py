# coding: utf-8
# python 3.7.0  x86_64

class MetaFoo(type):
    
    def __new__(cls, *args, **kwargs):
        print("meta  __new__ entering")
        _instance = super(MetaFoo, cls).__new__(cls, *args, **kwargs)
        print("meta  __new__ existing")
        return _instance
        
    def __init__(cls, *args, **kwargs):
        print("meta  __init__")
        super(MetaFoo, cls).__init__( *args, **kwargs)
    
    def __call__(cls, *args, **kwargs):
        print("meta  __call__ entering")
        _instance = super(MetaFoo, cls).__call__(*args, **kwargs)
        print("meta  __call__ existing")
        return _instance
        
        
class Foo(metaclass=MetaFoo):
    
    def __new__(cls):
        print("class __new__ entering")
        _instance = super(Foo, cls).__new__(cls)
        print("class __new__ existing")
        return _instance
        
    def __init__(self):
        print("class __init__")
    
    def __call__(cls, text=str):
        print("class __call__")
        print(text)
        print('----')
        return MetaFoo.__call__(Foo)
    
    def perceval(self):
        print("c'est pas faux")
    
if __name__ == '__main__':
    foo = Foo()
    a = foo("it's a joke ??!")
    b = a("Ho wait the code run o_O")
    c = b("it's magical !!")
    print(type(a), type(b), type(c), type(foo))
    
