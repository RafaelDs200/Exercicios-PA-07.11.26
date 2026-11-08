################################################################
# Descrição: Verificar o sexo através de uma letra digitada.
# Parâmetros de entrada: Uma letra (F ou M).
# Valores de saída: Feminino, Masculino ou Sexo Inválido.
# Autor: Rafael Dantas dos Santos
################################################################

letra = input("Digite F ou M: ").upper()

if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
else:
    print("Sexo Inválido")
