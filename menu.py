
from consultar_notas import consulta_codigo
from consultar_notas import consulta_nome

menu_num = { '1':'Consulta por código',
             '2':'Consulta por nome',
             '3':'Sair do prorgrama'}

def selecionar_menu():
    escolha_menu = 0
    print("Menu\n")

    while escolha_menu not in menu_num: 
        for chave in menu_num.keys():
            print(f'{chave} -> {menu_num[chave]}')
        
        escolha_menu = input('\nProfessor, escolha uma das opções do menu abaixo: ')

        if escolha_menu == '1':
            escolha_menu = 1
            consulta_codigo(escolha_menu)
            break
              
        elif escolha_menu == '2':
            escolha_menu = 2
            consulta_nome(escolha_menu)
            break
        
        elif escolha_menu == '3':
            print('\nPrograma encerrado')
            break 

        else: 
            print('\nEscolha invalida, digite uma das opções indicadas.')  
    return