################################################################
# Descrição: Mostra a tabuada de um número.
# Parâmetros de entrada: Um número escolhido pelo usuário.
# Valores de saída: Tabuada do número informado.
# Autor: Rafael Dantas dos Santos
################################################################

numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
