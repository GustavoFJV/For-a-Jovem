fruta = input("Escolha uma das frutas: ").lower()
match fruta:
    case "maça":
        print("é uma maçã")
    case "banana":
        print("é uma banana")
    case _:
        print("Escolha errada - é outra fruta")
