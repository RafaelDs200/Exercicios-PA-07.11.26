################################################################
# Descrição: Calcula a média de duas notas de um aluno.
# Parâmetros de entrada: Duas notas.
# Valores de saída: Média e situação do aluno.
# Autor: Rafael Dantas dos Santos
################################################################

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
