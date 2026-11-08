################################################################
# Descrição: Verificar se um número é positivo ou negativo.
# Parâmetros de entrada: Um número.
# Valores de saída: Positivo, negativo ou zero.
# Autor: Rafael Dantas dos Santos
################################################################

numero = float(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")
