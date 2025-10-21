opc=0


while True:
    print("1 - Para receber um Bom-Dia")
    print("2 - Para receber um Boa-Tarde")
    print("3 - Para receber um Boa - Noite")
    print("4 - Sair")
    opc = int(input("Introduza a opção: "))


    match opc :
        case 1:
            print("Bom-Dia")
        case 2:
            print("Boa-Tarde")
        case 3:
            print("Boa-Noite")
        case 4:
            print("Adeus!")
            break