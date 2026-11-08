################################################################
# Descrição: Receber dois números e mostrar o maior deles.
# Parâmetros de entrada: Dois números.
# Valores de saída: O maior número digitado.
# Autor: Rafael Dantas dos Santos
################################################################

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os dois números são iguais!")
