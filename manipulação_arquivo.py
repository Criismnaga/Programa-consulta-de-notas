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