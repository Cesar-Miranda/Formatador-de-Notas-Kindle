# [FORMATADOR DE NOTAS KINDLE EM PADRÃO ACADÊMICO ABNT DE CITAÇÃO e REFERÊNCIA]

# Função de Tratamento das notas
def tratamento_arquivo(arquivo):
    conteudo = []
    paginas = []
    checador_final = 0
    
    while arquivo != '':
      
        # Encontrando strings que caracterizam o início e o fim do texto contido na nota
        inicio = arquivo.find("  ")
        inicio +=2
        final = arquivo.find(" =")
        
        # Encontrando o número das páginas
        inicio_pagina = arquivo.find("posição ")
        inicio_pagina = inicio_pagina + 7
        fim_pagina = arquivo.find(" |")
        pagina = arquivo[inicio_pagina+1:fim_pagina]
        meio_pagina = pagina.find("-")
        paginas.append(pagina)

        # Consultando se o arquivo terminou
        if "=" not in arquivo[inicio:final]:
            conteudo.append(arquivo[inicio:final])
            arquivo = arquivo[final+2:]
            
        if " =" not in arquivo:
            if checador_final == 0:
                checador_final = 1
            else:
                break
 
    return conteudo, paginas


# Função Principal de execução
if __name__ == "__main__":
    
    # input das notas
    arquivo_bruto = input('Coloque aqui as notas a serem formatadas: ')

    # Cadastramento de dados que, ou não vem nas notas, ou não são confiáveis (como no caso de pdfs salvos com nomes diferentes do título da obra)
    while True:
        nota_formatada = {}
        nota_formatada['titulo'] = input('Qual é o nome do livro a ser referenciado? ')
        nota_formatada['autor'] = input('Informe o "SOBRENOME, Autor": ')
        nota_formatada['editora'] = input('Qual é a editora do livro? ')
        nota_formatada['edicao'] = input('Qual é a edição do livro? ')
        nota_formatada['ano'] = input('Qual é o ano do livro? ')

        # Chamamento e retorno da função
        arquivo_tratado, paginas_tratadas = tratamento_arquivo(arquivo_bruto)

        # Listas de conteúdos e páginas adicionados aos seus respectivos campos no dicionário
        nota_formatada['conteudo'] = arquivo_tratado
        nota_formatada['pagina'] = paginas_tratadas
        
        # Output como as notas formatadas. Obs.: As páginas serão as do e-book, não as do livro físico.
        try:
            for i in range(len(nota["conteudo"])):
                print("\n")
                print(f' {nota_formatada["conteudo"][i]} ({nota_formatada["autor"]}. {nota_formatada["ano"]}. P. {nota_formatada["pagina"][i]})')
        except:
            pass
          
        # Output com as referências prontas
        print(f'Referências:')
        print(f'{nota_formatada["autor"]}. {nota_formatada["titulo"]}. {nota_formatada["edicao"]} Ed. {nota_formatada["editora"]}, {nota_formatada["ano"]}.')

        # Consultar sobre nova formatação de notas
        repetir = input("Deseja formatar outro arquivo? [S/N] ")
        while repetir not in "SsNn":
            repetir = input("Resposta inválida. tente novamente. Você deseja formatar outro arquivo? [S/N] ")
        if repetir in "Ss":
            continue
        elif repetir in "Nn":
            print("Estou feliz por poder ajudar. Até a próxima!")
            break
