def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print("Erro: por favor, digite um número inteiro válido.")
            continue
        else:
            return n

def linha(tam=52):
    return '-' * tam

def cabecalho(txt):
    print (linha())
    print (txt.center(55))
    print (linha())

def cabecalho_consulta_dado(txt):
    print(txt.center(55))
    print(linha())

def cabecalho_total(txt):
    print(linha())


def menu(lista):
    cabecalho("Selecione o que deseja")
    c=1
    for item in lista:
        print(f"{c} - {item}")
        c+=1
    print(linha())
    opc=leiaInt("Sua Opçao: ")
    return opc
    


 
    
