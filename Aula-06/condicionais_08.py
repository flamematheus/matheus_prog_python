import os
os.system("cls")

nota_01 = 9
nota_02 = 7
nota_03 = 5
nota_04 = 9

media = (nota_01 +nota_02+nota_03+nota_04 )/4

if (media >= 7):
    print(f"media {media},Aluno Aprovado com sucesso !")

elif(media >=5 and media < 7 ):
    print(f"media {media},aluno de recuperação")

else :
    print(f"media {media}, Aluno Reprovado com sucesso !")
