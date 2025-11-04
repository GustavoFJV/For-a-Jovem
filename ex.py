media = float(input("Média:"))
if(media >= 7):
    x = "Aprovado"
elif (media >=5): #elif ; se nao ser (junção de else com if)
    x = "Recuperação"
else:
    x= "Reprovado"
print("Média: ",media)
print("Situação: ", x)
'''
#media =int(input("digite a media do aluno"))
#if media >= 7 :
#print("Aprovado")
#elif media >=5:
#print ("Recuperação")
#else:
#print("Reprovado")

