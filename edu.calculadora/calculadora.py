import math
class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            return "Erro"
        return a / b
    
    def porcentagem(self, valor, percentual):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, a):
        return math.sqrt(a)
    
    def potenciacao(self, base, expoente):
        return base ** expoente

calc = Calculadora()
n= int(input("Digite um número: "))
n2= int(input("Digite um número: "))
n3= int(input("Digite o número a ser feito a raiz quadrada: "))
n4= int(input("Digite o número base da potencia : "))
n5= int(input("Digite o expoente : "))
n6= int(input("Digite o valor da porcentagem : "))
n7= int(input("Digite o percentual : "))
print("Soma:", calc.soma(n, n2))               
print("Subtração:", calc.subtracao(n, n2))     
print("Multiplicação:", calc.multiplicacao(n, n2))  
print("Divisão:", calc.divisao(n, n2))        
if n2 == 0:
    print("Divisão por zero:", calc.divisao(n, n2))
print("Porcentagem:", calc.porcentagem(n6, n7))  
print("Raiz Quadrada:", calc.raiz_quadrada(n3))   
print("Potenciação:", calc.potenciacao(n4, n5))    