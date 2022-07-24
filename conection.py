from operator import truediv


def conect():
    import mysql.connector
    try:
        conexao = mysql.connector.connect(host='localhost',database='petinder_fase_2',user='root',password='08147742vd7xtu')
        return conexao
    except:
        print('erro ao conectar')
        