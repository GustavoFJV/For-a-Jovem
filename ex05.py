preço =float(input("Digite o valor do produto"))
if (preço <=100) :
    desconto = preço * 0.10 
    preco_final = preço - desconto
    print(f"desconto de 10% aplicado R$ {desconto}! Valor aplicado com desconto:R$ {preco_final}")
else (preço >=100) :
    desconto = preço * 0.20
    preco_final = preço - desconto
    print(f"desconto de 20% aplicado R$ {desconto}! Valor aplicado com desconto:R$ {preco_final}")
    """
    #preço = float(input("Preço: R$))
    if (preço <=100):
        desc = preco * 0.1
    else:
        desc+ preco * 0.2 
    novo_valor = preco - desc
    print ("Preço R$ ", preco)
    print(Desconto : R$" , desc)
    print(Novo Preço : R$ " , novo_valor)