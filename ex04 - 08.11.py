################################################################
# Descrição: Identificar o turno de estudo.
# Parâmetros de entrada: Uma letra (M, V ou N).
# Valores de saída: Saudação correspondente ao turno.
# Autor: Rafael Dantas dos Santos
################################################################

turno = input("Digite M, V ou N: ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
