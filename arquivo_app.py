from cabecalho_exercicio import *
def arquivoExiste(arquivo):
    try:
        a = open (arquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arquivo):
    try:
        a = open(arquivo, "wt+")
        a.close()
    except:
        print("Houve um Erro na criação do arquivo!")
    else:
        print("Arquivo criado com sucesso!")

def lerArquivo(arquivo):
    try:
        a = open (arquivo, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("Situação atual no Sudeste")
        cabecalho_consulta_dado("Prof. de Saúde    População")
        for linha in a:
            dado = linha.split(";")
            print(f'{dado[0]:<20}{dado[1]:<15}{dado[2]}')
          
    finally:
        #função que apresenta a linha tracejada para separar os dados
        cabecalho_total("")
        print(f'Total de Prof. de Saude {dado[3]}')
        print(f'Total da população em geral{dado[4]}')
        a.close()

def cadastrar(arq, estado, prof_saude,pop_geral, total_prof_saude,total_pop_geral):
    try:
        a = open(arq, "at")
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write (f'{estado};{prof_saude}; {pop_geral};{total_prof_saude}; {total_pop_geral}\n')
        except:
            print("Houve um erro na hora de escrever os dados!")
        else :
                print("Novo registro adicionado.")
        a.close()
             

