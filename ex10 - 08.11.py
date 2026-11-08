################################################################
# Descrição: Apresenta todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20.
# Parâmetros de entrada: Não recebe valores.
# Valores de saída: Os números ímpares compreendidos entre 0 e 20.
# Autor: Rafael Dantas dos Santos
################################################################

for numero in range(0, 21):
    if numero % 2 != 0:
        print(numero)
