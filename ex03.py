'''
o usuário entra com 2 valores inteiros e o programa responde quem é o maior entre eles
programa responde se :
Primeiro valor é maior que o segundo valor
Segundo valor é maior que o primeiro
primeiro valor é igual ao segundo valor
'''
x = int(input("Escolha o primeiro valor"))
y = int(input("Escolha o segundo valor"))
if (x==y) :
    print(f"O número {x} é igual ao número {y}")
elif (x > y) :
    print(f"O número {x} é maior que o número {y}")
else: 
    print(f"O número {x} é menor que o número {y}")