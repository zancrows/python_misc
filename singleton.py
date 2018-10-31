# coding: utf-8
# python 3.7.0 x86_64

class SingletonClass:   
    _instance = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance[cls]
    
    def __init__(self):
        self.foo = "hello world"
        

def main():
    singleton = SingletonClass()
    singleton_2 = SingletonClass()
    
    print(singleton is singleton_2)
    print(singleton == singleton_2)
    
if __name__ == "__main__":
    main()
