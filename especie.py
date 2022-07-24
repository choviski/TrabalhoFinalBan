import conection

conexao = conection.conect()

def all():
    print("\n" * 130)
    if(conexao):
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("select * from Especies;")
        linha = cursor.fetchall()
        print('--------------------------------------------------------------------------------------------')
        print('|                                      Espécies                                            |')
        print('--------------------------------------------------------------------------------------------\n\n')
        print('\tid\t Nome \t\tDescricao')
        print()
        for a in linha:
            print("\t",a['id'],"\t",a['nome'],"\t\t",a['descricao'])
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
            sql = "INSERT INTO Especies(nome,descricao) VALUES(%s, %s)"
            valores = (dados['nome'], dados['descricao'])
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

