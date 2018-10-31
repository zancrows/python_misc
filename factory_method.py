# coding: utf-8
# python 3.7.0 x86_64

import abc

class Soldier(abc.ABC):
    
    _number = 0
    
    @abc.abstractmethod
    def __init__(self):
        self.name = None
        self.id = None
    
    def __str__(self):
        return f"I'm {self.name} {self.id}"
    
class Knight(Soldier):

    def __init__(self):
        Knight._number += 1
        self.id  = Knight._number
        self.name = "Knight"
    
class Pikeman(Soldier):

    def __init__(self):
        Pikeman._number += 1
        self.id = Pikeman._number
        self.name = "Pikeman"
    

# Factory
class Barraks():
    _soldiers = {"Knight": Knight, "Pikeman": Pikeman}
    
    @staticmethod
    def get_soldier(soldier_type):
        return Barraks._soldiers.get(soldier_type)()

def main():
    c1 = Barraks.get_soldier("Knight")
    c2 = Barraks.get_soldier("Knight")
    c3 = Barraks.get_soldier("Knight")
    print(c1)
    print(c2)
    print(c3)
    
    p1 = Barraks.get_soldier("Pikeman")
    p2 = Barraks.get_soldier("Pikeman")
    print(p1)
    print(p2)

    
if __name__ == "__main__":
    main()
    