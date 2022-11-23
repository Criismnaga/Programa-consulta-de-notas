from manipulação_arquivo import arquivo_para_lista
def arquivo_para_lista(): 

    classe = open('arquivos\classe.txt', 'r')
    notas = open('arquivos\\notas.txt', 'r')

    linha1 = 0
    linha2 = 0
    lista_aluno = []
    lista_nota = []

    for linha1 in classe:
        linha1.strip()
        codigo_aluno = linha1.split()
        lista_aluno.append(codigo_aluno) 

    for linha2 in notas:
        linha2.strip()
        nota_aluno = linha2.split()
        lista_nota.append(nota_aluno)

    classe.close()
    notas.close()
    
    return lista_aluno, lista_nota

def consulta_codigo(escolha_menu):

    lista_aluno, lista_nota = arquivo_para_lista()
    i = 0

    while escolha_menu == 1:
        codigo_input = input("\nDigite o código do Aluno: ")

        for i in range(len(lista_aluno)): 

            if codigo_input == lista_aluno[i][0]:
                print(f'\nO aluno {lista_aluno[i][1]} codigo {lista_aluno[i][0]} possui as seguintes notas: {(lista_nota[i])}')
                escolha_menu = 3  
    return

def consulta_nome(escolha_menu):

    lista_aluno, lista_nota = arquivo_para_lista()
    i = 0
   
    while escolha_menu == 2:
        nome_input = input("\nDigite o nome do Aluno: ")

        for i in range(len(lista_aluno)): 
            
            if nome_input == lista_aluno[i][1]:
                print(f'\nO aluno {lista_aluno[i][1]} codigo {lista_aluno[i][0]} possui as seguintes notas: {(lista_nota[i])}')
                escolha_menu = 3 
    return







    
    









