import conection

conexao = conection.conect()


def all():
    print("\n" * 130)
    if (conexao):
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT Animais.id as id, Animais.nome as nome, Animais.sexo as sexo, Animais.idade as idade, Animais.porte as porte, Animais.pelagem as pelagem, Racas.nome as raca, Especies.nome as especie from Animais join Racas on Racas.id = Animais.id_raca join Especies on Racas.id_especie = Especies.id"
        )
        linha = cursor.fetchall()
        print(
            '------------------------------------------------------------------------------------------------------------------------'
        )
        print(
            '|                                                           Animais                                                     |'
        )
        print(
            '-------------------------------------------------------------------------------------------------------------------------\n\n'
        )
        print(
            '\tid\t Nome \t\tSexo \t\t\tIdade\t\tPorte\t\tPelagem\t\tRaça\t\tEspécie'
        )
        print()
        for a in linha:
            print("\t", a['id'], "\t", a['nome'], "\t", a['sexo'], "\t\t",
                  a['idade'], "\t\t", a['porte'], "\t\t", a['pelagem'], "\t\t",
                  a['raca'], "\t\t", a['especie'])
        print(
            '\n--------------------------------------------------------------------------------------------'
        )
        input('\n\n\nPessione Enter para voltar ao menu.....')
    else:
        print("Problema de conexao")
        input('\n\n\nPessione Enter para voltar ao menu.....')


def create(dados):
    print("\n" * 130)
    if (conexao):
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO Animais(nome,idade,sexo,porte,pelagem,id_raca) VALUES(%s, %s, %s, %s, %s, %s)"
            valores = (dados['nome'], int(dados['idade']), dados['sexo'],
                       dados['porte'], dados['pelagem'], int(dados['id_raca']))
            cursor.execute(sql, valores)
            conexao.commit()
            print('Dados inseridos com sucesso')
            input('\n\n\nPessione Enter tecla para voltar ao menu.....')
        except:
            print("Erro ao insirir os dados na tabela")
            input('\n\n\nPessione Enter para voltar ao menu.....')
    else:
        print("Problema de conexao")
        input('\n\n\nPessione qualquer tecla para voltar ao menu.....')


def infoAnimalMaisVelho():
    print("\n" * 130)
    print("\n" * 130)
    if (conexao):
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT Animais.id as id, Animais.nome as nome, Animais.idade as idade, Animais.sexo as sexo, Animais.porte as porte, Animais.pelagem as pelagem, Racas.descricao as raca, Especies.descricao as especie from Animais JOIN Racas on Animais.id_raca = Racas.id JOIN Especies on Especies.id = Racas.id_especie WHERE Animais.idade in (SELECT MAX(idade) from Animais)"
        )
        linha = cursor.fetchall()
        print(
            '------------------------------------------------------------------------------------------------------------------------'
        )
        print(
            '|                                                           Animais                                                     |'
        )
        print(
            '-------------------------------------------------------------------------------------------------------------------------\n\n'
        )
        print(
            '\tid\t Nome \t\tSexo \t\t\tIdade\t\tPorte\t\tPelagem\t\tRaça\t\tEspécie'
        )
        print()
        for a in linha:
            print("\t", a['id'], "\t", a['nome'], "\t", a['sexo'], "\t\t",
                  a['idade'], "\t\t", a['porte'], "\t\t", a['pelagem'], "\t\t",
                  a['raca'], "\t\t", a['especie'])
        print(
            '\n--------------------------------------------------------------------------------------------'
        )
        input('\n\n\nPessione Enter para voltar ao menu.....')
    else:
        print("Problema de conexao")
        input('\n\n\nPessione Enter para voltar ao menu.....')
