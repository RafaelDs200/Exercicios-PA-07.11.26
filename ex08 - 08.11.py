################################################################
# Descrição: Soma os 100 primeiros números naturais.
# Parâmetros de entrada: Não recebe valores.
# Valores de saída: Soma dos números de 1 até 100.
# Autor: Rafael Dantas dos Santos
################################################################

soma = 0

for numero in range(1, 101):
    soma = soma + numero

print("A soma dos números é:", soma)
