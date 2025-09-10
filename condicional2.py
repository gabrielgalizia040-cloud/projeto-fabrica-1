# crie um codigo que receba 3 notas, calculando a media
# e informe se o aluno esta aprovado, em recuperacao
# ou reprovado
# obs: aprovadomedia >= 7

# recuperacao media > 4
# reprovado media < 4

# etapas
# 1) solicitar as notas nao usuario
primeira_nota = float(input("digite a primeira mota: "))
sugunda_nota = float(input("digite a segunda nota: "))
terceira_nota = float(input("digite a terceira nota: "))

# 2) calcular a media 
media = (primeira_nota + sugunda_nota + terceira_nota) /3

# 3) checar a condicao do aluno
if media >=7:
    print(f"o aluno tem media {media:.2f} e esta aprovado.")
elif media > 4:
    print(f"o aluno teve media {media:.2f} e esta aprovado. ")
else:
    print(f"o aluno teve media {media:.2f} e esta reprovado.")
    