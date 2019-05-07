# coding: utf-8
# python 3.7.1 x86_64

class Calcul2Int:

    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b

    @property
    def result(self):
        raise NotImplementedError


class Add2Int(Calcul2Int):

    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def result(self) -> int:
        return self.a + self.b

class Sous2Int(Calcul2Int):

    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def result(self) -> int:
        return self.a - self.b

class DecoratorCalcul2Int(Calcul2Int):

    def __init__(self, calcul):
        super().__init__(calcul.a, calcul.b)
        self.calcul = calcul

class Calcul2IntWithMul(DecoratorCalcul2Int):

    def __init__(self, calcul, multi):
        super().__init__(calcul)
        self.multi = multi

    @property
    def result(self) -> int:
        return self.calcul.result * self.multi


if __name__ == "__main__":
    a = Add2Int(10,5)
    a = Calcul2IntWithMul(a, 2)
    print(a.result)
    # >>> 30

    b = Sous2Int(15, 10)
    b = Calcul2IntWithMul(b, 3)
    print(b.result)
    # >>> 15

