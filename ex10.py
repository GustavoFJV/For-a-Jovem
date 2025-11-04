x = int(input("primero valor: "))
y = int(input("segundo valor: "))
print(" + soma")
print(" - subtração")
print(" * multiplicação")
print(" / divisão")
op = input("Escolha uma operação: ")
match op:
    case "+" :
        soma = x + y 
        print(f"{x}+ {y} = {soma}")
    case "-" :
        multiplicação = x * y
        print(f"{x} * {y} = {multiplicação}")
    case "-" :
        print(f"{x} - {y}= {subtração}")
    case "/" :
      print(f"{x} / {y}= {divisão}")
    