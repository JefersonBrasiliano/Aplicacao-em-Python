from cabecalho_exercicio import *
from arquivo_app import *
total_prof_saude = 0
total_pop_geral = 0

arq = "arquivo.txt"

if not arquivoExiste (arq):
    criarArquivo(arq)    
while True:
    resposta = menu(["Adicionar infectadoss em São Paulo","Adicionar infectadoss no Rio de Janeiro", "Adicionar infectadoss no Espírito Santo", "Adicionar infectadoss casos em Minas Gerais", "Consultar situação atual na região", "Sair do programa"])
    if resposta ==1:
        estado = "São Paulo"
        prof_saude = int (input ("Informe a quantidade de profissionais da saúde infectados:"))
        pop_geral = int (input ("Informe a quantidade de pessoas em geral infectados:"))
        total_prof_saude += prof_saude
        total_pop_geral += pop_geral
        cadastrar(arq, estado, prof_saude,pop_geral, total_prof_saude,total_pop_geral)
        
        
    elif resposta==2:
        estado = "Rio de Janeiro"
        prof_saude = int (input ("Informe a quantidade de profissionais da saúde infectados:"))
        pop_geral = int (input ("Informe a quantidade de pessoas em geral infectados:"))
        total_prof_saude += prof_saude
        total_pop_geral += pop_geral
        cadastrar(arq, estado, prof_saude, pop_geral,total_prof_saude,total_pop_geral)
    elif resposta==3:
        estado = "Espirito Santo"
        prof_saude = int (input ("Informe a quantidade de profissionais da saúde infectados:"))
        pop_geral = int (input ("Informe a quantidade de pessoas em geral infectados:"))
        total_prof_saude += prof_saude
        total_pop_geral += pop_geral
        cadastrar(arq, estado, prof_saude, pop_geral,total_prof_saude,total_pop_geral)
    elif resposta==4:
        estado = "Minas Gerais"
        prof_saude= int (input ("Informe a quantidade de profissionais da saúde infectados:"))
        pop_geral=  int (input ("Informe a quantidade de pessoas em geral infectados:"))
        total_prof_saude += prof_saude
        total_pop_geral += pop_geral
        cadastrar(arq, estado, prof_saude, pop_geral,total_prof_saude,total_pop_geral)
    elif resposta==5:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
        break
    elif resposta==6:
        print ("Saindo do sistema!")
        break
    else:
        print ("Erro!, por favor digite uma opção válida")


  
 
    
        
        
