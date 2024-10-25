class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        mdc = self.calcula_mdc(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc

    def calcula_mdc(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, other):
        num = self.numerador * other.denominador + self.denominador * other.numerador
        den = self.denominador * other.denominador
        return Fracao(num, den)

    def __sub__(self, other):
        num = self.numerador * other.denominador - self.denominador * other.numerador
        den = self.denominador * other.denominador
        return Fracao(num, den)

    def __mul__(self, other):
        num = self.numerador * other.numerador
        den = self.denominador * other.denominador
        return Fracao(num, den)

    def __truediv__(self, other):
        num = self.numerador * other.denominador
        den = self.denominador * other.numerador
        return Fracao(num, den)

    def __eq__(self, other):
        return self.numerador == other.numerador and self.denominador == other.denominador

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.numerador * other.denominador < other.numerador * self.denominador

    def __le__(self, other):
        return self.numerador * other.denominador <= other.numerador * self.denominador

    def __gt__(self, other):
        return self.numerador * other.denominador > other.numerador * self.denominador

    def __ge__(self, other):
        return self.numerador * other.denominador >= other.numerador * self.denominador

# Exemplos de uso
soma = Fracao(1, 2) + Fracao(3, 4)
mult = Fracao(1, 2) * Fracao(3, 4)
sub = Fracao(1, 2) - Fracao(3, 4)
div = Fracao(1, 2) / Fracao(3, 4)

print(soma)
print(mult)
print(sub)
print(div)

# Exemplos de uso
f1 = Fracao(1, 2)
f2 = Fracao(3, 4)


print(f1 == f2)  # False
print(f1 != f2)  # True
print(f1 < f2)   # True
print(f1 <= f2)  # True
print(f1 > f2)   # False
print(f1 >= f2)  # False