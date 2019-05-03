# coding: utf-8
# python 3.7.1 x86_64

from abc import ABCMeta, abstractmethod

class StrategyCalc(metaclass=ABCMeta):

    @abstractmethod
    def calc(self):
        raise NotImplementedError

class StratAdd:

    def calc(self):
        return self.a + self.b

class StratSous:

    def calc(self):
        return self.a - self.b


class Calcul:

    def __init__(self, a, b, strategy=None):
        self.a = a
        self.b = b
        self.strategy = strategy

    def calc(self):
        if self.strategy:
            return self.strategy.calc(self)
        else:
            raise ValueError("pas de strategy")

if __name__ == "__main__":

    c = Calcul(4, 5, StratAdd)
    print(c.calc())
    # >>> 5
    c.strategy = StratSous
    print(c.calc())
    # >>> -1




