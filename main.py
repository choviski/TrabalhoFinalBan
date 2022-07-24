import time
import especie
import raca
import animal

def MostraMenu():
    print("\n" * 130)
    print('--------------------------------------------------------------------')
    print('|                             Menu                                 |')
    print('--------------------------------------------------------------------')
    print('| 1 - \t Mostrar Todas as raças                                    |')
    print('| 2 - \t Mostrar Todas as Espécies                                 |')
    print('| 3 - \t Mostrar Todas os Animais                                  |')
    print('| 4 - \t Inserir novo Animal                                       |')
    print('| 5 - \t Inserir nova Espécie                                      |')
    print('| 6 - \t Inserir nova Raça                                         |')
    print('| 7 - \t Mostrar infermações sobre animais com maior idade         |')
    print('| 8 - \t Sair                                                      |')
    print('--------------------------------------------------------------------\n')

while(True):
    MostraMenu()
    opcao = input()
    if(opcao == '1'):
        raca.all()
    elif(opcao == '2'):
        especie.all()
    elif(opcao == '3'):
        animal.all()
    elif(opcao == '4'):
        raca.all()
        dados = {
            'nome':input('Insira o nome do animal: '),
            'idade':input('Insira o idade do animal: '),
            'sexo':input('Insira o sexo do animal: '),
            'pelagem':input('Insira o pelagem do animal: '),
            'porte':input('Insira o porte do animal: '),
            'id_raca':input('Insira o id da raca do animal: ')
        }
        animal.create(dados)
    elif(opcao == '5'):
        especie.create({"nome": input('Insira o nome da Espécie: '), "descricao": input('Insira a descricao da Espécie: ')})
    elif(opcao == '6'):
        especie.all()
        dados = {
            'nome':input('Insira o nome da raça: '),
            'descricao':input('Insira a descrição da Raca: '),
            'id_especie':input('Insira o id da espécie: ')
        }
        raca.create(dados)
    elif(opcao == '7'):
        animal.infoAnimalMaisVelho()
    elif(opcao == '8'):
        break
    else:
        print('Opção inválida, digite novamente....')
        time.sleep(1)


