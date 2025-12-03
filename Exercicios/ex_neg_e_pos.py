numero = int(input("Digite um número: "))

match numero:
    case n if n < 0:
        print("negativo")

    case 0:
        print("zero")

    case n if n > 0:
        # positivo
        if n % 3 == 0 and n % 5 == 0:
            print("divisível por 3 e 5")
        elif n % 2 == 1:
            print("positivo e impar")
        elif n % 2 == 0:
            print("positivo e par")
        else:
            print("outros números positivos")
