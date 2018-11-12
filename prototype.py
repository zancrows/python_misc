# coding: utf-8
# python 3.7.0 x86_64

import copy
import random

get_id = lambda: random.randint(1_000_000, 9_999_999)

class Prototype:
    
    def clone(self, **kwargs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(kwargs)
        
        return obj


class ComplexObject1(Prototype):
    
    def __init__(self,id:int=get_id()):
        self.id = id
    
    def __str__(self):
        return f"i'm a complex object ONE, id: {self.id}"

        
class ComplexObject2(Prototype):
    
    def __init__(self,id:int=get_id()):
        self.id = id
    
    def __str__(self):
        return f"i'm a complex object TWO, id: {self.id}"

class PrototypeFactory():
    
    _instances = {}
    
    @staticmethod
    def get_obj(name:str, **kwargs):
        return PrototypeFactory._instances[name].clone(**kwargs)
        
    @staticmethod
    def initialize():
        PrototypeFactory._instances["ComplexObject1"] = ComplexObject1()
        PrototypeFactory._instances["ComplexObject2"] = ComplexObject2()
        

def main():
    PrototypeFactory.initialize()
    a = PrototypeFactory.get_obj("ComplexObject1", id=get_id())
    b = PrototypeFactory.get_obj("ComplexObject1", id=get_id())
    c = PrototypeFactory.get_obj("ComplexObject2", id=get_id())
    
    print(PrototypeFactory._instances["ComplexObject1"])
    print(a)
    print(b)
    print(PrototypeFactory._instances["ComplexObject2"])
    print(c)


if __name__ == "__main__":
    main()