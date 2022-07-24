import conection

conexao = conection.conect()

def all():
    print("\n" * 130)
    if(conexao):
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("select Racas.id as id, Racas.nome as nome, Racas.descricao as descricao, Especies.nome as especie from Racas join Especies on Especies.id = Racas.id_especie;")
        linha = cursor.fetchall()
        print('--------------------------------------------------------------------------------------------')
        print('|                                       Raças                                              |')
        print('--------------------------------------------------------------------------------------------\n\n')
        print('\tid\t Nome \t\tDescricao \t\t\tEspécie')
        print()
        for a in linha:
            print("\t",a['id'],"\t",a['nome'],"\t",a['descricao'],"\t\t",a['especie'])
        print('\n--------------------------------------------------------------------------------------------')
        input('\n\n\nPessione Enter para voltar ao menu.....')
    else:
        print("Problema de conexao")
        input('\n\n\nPessione Enter para voltar ao menu.....')

def create(dados):
    print("\n" * 130)
    if(conexao):
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO Racas(nome,descricao,id_especie) VALUES(%s, %s, %s)"
            valores = (dados['nome'], dados['descricao'], int(dados['id_especie']))
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