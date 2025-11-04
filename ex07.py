nome = (input("Digite o Nome: "))
Salario = float(input("Digite o salario: ")) 
#desconto
if Salario >= 3000:
    desconto = Salario * 0.11
elif Salario >= 2000:
    desconto = Salario * 0.09
else: 
    Salario < 2000
    desconto = Salario * 0.08
#vale
if Salario >= 2000:
    vale = Salario * 0.06
else:
    vale = Salario * 0.05
#bonus
if Salario >= 3000:
    bonus = 300
else:
    bonus = 200
#cargo
if Salario >= 3000:
    cargo = "Acionista"
elif Salario >= 2000:
    cargo = "Gerente"
else: 
    cargo = "Vendedor"

salarioliquido = Salario - (desconto + vale) + bonus
#salarioliquido = salario - inss - valle + bonus

#saídas:
print(f"Nome do colaborador: {nome}")
print(f"Salario: {Salario}")
print(f"desconto: {desconto}")
print(f"vale: {vale}")
print(f"bonus: {bonus}")
print(f"cargo: {cargo}")
print(f"salarioliquido: {salarioliquido}")



