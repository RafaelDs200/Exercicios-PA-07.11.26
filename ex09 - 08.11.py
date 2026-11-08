################################################################
# Descrição: Soma os números pares de 1 até 500.
# Parâmetros de entrada: Não recebe valores.
# Valores de saída: Soma dos números pares de 1 até 500.
# Autor: Rafael Dantas dos Santos
################################################################

soma = 0

for numero in range(1, 501):
    if numero % 2 == 0:
        soma = soma + numero

print("A soma dos números pares é:", soma)
