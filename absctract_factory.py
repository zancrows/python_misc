# coding: utf-8
# python 3.7.0 x86_64

import abc

# abstract factory
class MilitaryBuilding(abc.ABC):
    
    @staticmethod
    def get_building(building_type=None):
        if building_type == "Barraks":
            return Barraks()
        elif building_type == "Archery":
            return Archery()
        else:
            raise NotImplementedError("This class does not exist")
    
    @abc.abstractmethod
    def get_soldier(soldier_type):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def get_shooter(shooter_type):
        raise NotImplementedError()


class Soldier(abc.ABC):
    _number = 0
    
    @abc.abstractmethod
    def __init__(self):
        self.name = None
        self.id = None
    
    def __str__(self):
        return f"I'm solder {self.name} {self.id}"
    
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
    
# concrete factory 1
class Barraks(MilitaryBuilding):
    _soldiers = {"Knight": Knight, "Pikeman": Pikeman}
    
    def get_soldier(self, soldier_type):
        return Barraks._soldiers.get(soldier_type)()
        
    def get_shooter(self, shooter_type):
        raise NotImplementedError()
        
        
class Shooter(abc.ABC):
    _number = 0
    
    @abc.abstractmethod
    def __init__(self):
        self.name = None
        self.id = None
    
    def __str__(self):
        return f"I'm shooter {self.name} {self.id}"
        
class Archer(Shooter):

    def __init__(self):
        Archer._number += 1
        self.id  = Archer._number
        self.name = "Archer"
    
class Lancer(Shooter):

    def __init__(self):
        Lancer._number += 1
        self.id = Lancer._number
        self.name = "Lancer"
    
# concrete factory 2
class Archery(MilitaryBuilding):
    _shooters = {"Archer": Archer, "Lancer": Lancer}
    
    def get_shooter(self, shooter_type):
        return Archery._shooters.get(shooter_type)()
        
    def get_soldier(self, soldier_type):
        raise NotImplementedError()

def main():
    barraks = MilitaryBuilding.get_building("Barraks")
    
    list_of_soldier = ["Knight"] * 3 + ["Pikeman"] * 2
    soldiers = [barraks.get_soldier(t) for t in list_of_soldier]
    for s in soldiers : print(s)
    
    archery = MilitaryBuilding.get_building("Archery")
    
    list_of_shooter = ["Archer"] * 2 + ["Lancer"] * 4
    shooters = [archery.get_shooter(s) for s in list_of_shooter]
    for s in shooters: print(s)
    
    
if __name__ == "__main__":
    main()
    
