print ("Selecione a opção")
print ("1 - par ou ímpar.")
print ("2 - maior ou menor.")
print ("3 - veja o dobro.")op = int(input("Digite o número: "))
match op:
    case 1:
        num = int(input("Escolha um número: "))
        if num %2 ==0:
            print (f"{num} é par.") #print(num, "é par.")
        else:
            print (f"{num} é ímpar.") #print(num, "é ímpar.")
    case 2:
        x = int(input("Escolha o primeiro número: "))
        y = int(input("Escolha o segundo número: "))
        if x > y:
            print (f"{x} é maior que {y}")
        elif x < y:
            print (f"{x} é maior que{y}")    
        else:          
            print (f"{x} é igual a {y}")
    case 3:
        a = int(input("Escolha um número: "))  
        dobro = a * 2 
    print(f"Opção {a} é {dobro}")  
    case _:
    print("Opção inválida")

