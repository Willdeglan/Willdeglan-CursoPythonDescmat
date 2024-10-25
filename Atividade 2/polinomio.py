class Polinomio:
    def __init__(self, expressao):
        self.expressao = expressao

    def __str__(self):
        return self.expressao

    def __add__(self, other):
        return Polinomio(f"{self.expressao} + {other.expressao}")

    def __sub__(self, other):
        return Polinomio(f"{self.expressao} - {other.expressao}")

    def __mul__(self, other):
        return Polinomio(f"{self.expressao} * {other.expressao}")

    def avaliar(self, x):
        return eval(self.expressao.replace("x", str(x)))

    def __eq__(self, other):
        # Simplificação básica para verificar igualdade
        return eval(self.expressao.replace("x", "1")) == eval(other.expressao.replace("x", "1"))

    def __repr__(self):
        return f"Polinomio('{self.expressao}')"

    def salvar_csv(self, a, b, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("x,f(x)\n")
            for i in range(a, b + 1):
                arquivo.write(f"{i},{self.avaliar(i)}\n")

# Exemplos de uso
p1 = Polinomio("2 * x**2 + 3 * x - 5")
p2 = Polinomio("x**2 - 2")
p3 = Polinomio("2 * x**2 + 3 * x - 5")

soma = p1 + p2
subtracao = p1 - p2
multiplicacao = p1 * p2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)

# Avaliação de um polinômio
x = 2
print(f"Avaliação de {p1} para x = {x}: {p1.avaliar(x)}")

# Comparação de igualdade
print(f"O polinômio {p1} é igual a {p2}: {p1 == p2}")
print(f"O polinômio {p1} é igual a {p3}: {p1 == p3}")

# Salvando resultados em um arquivo CSV
p1.salvar_csv(0, 5, "polinomio.csv")
print("Dados salvos no arquivo polinomio.csv")
