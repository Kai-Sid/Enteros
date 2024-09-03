class CalculadoraMCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular_mcd(self):
        a, b = self.a, self.b
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

# Ejemplo de uso:
if __name__ == "__main__":
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    calculadora = CalculadoraMCD(num1, num2)
    mcd = calculadora.calcular_mcd()
    print(f"El máximo común divisor de {num1} y {num2} es {mcd}.")

