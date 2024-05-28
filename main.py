import os
LINHA = '*'*30


def inserir_placas():
    menu_banco()

def ler_arquivo():
    menu_banco()

def atualizar_placas_carros():
    menu_banco()

def validar_dados_base():
   menu_banco()

def encerrar_bot():
    os.system('clear')
    os.system('exit')

def menu_banco():
    '''Menu para cada banco separado do sistema Notion'''

    os.system('clear')
    print(LINHA)
    print('Validar dados do Banco de dados')
    print(LINHA)

    print('\nseleciona qual banco vai mexer')
    print('1- Banco de expedição')
    print('2- Banco eletronico ')
    print('3- Banco ipva')
    print('4- Voltar para menu principal \n')

    opcao = int(input('Digite numero da opção desejada :'))
    if opcao == 4 : return main()
    return opcao

def opcoes_menu():
    '''Função para realizar acionamento do BOT'''
    
    os.system('clear')
    print(LINHA)
    print('Menu de Seleção')
    print(LINHA)
    print('1 - Inserir novas placas')
    print('2 -Ler arquivo de csv')
    print('3 -Atualizar placas Carros')
    print('4 -Validar os dados da base')
    print('5 -Encerrar Zebetio')

    opcao = int(input('\nDigite numero da opção desejada :'))

    return chamada_funcoes(opcao)

def chamada_funcoes(opcao):
    '''Funcão para fazer a chamada das funções e suas logicas '''

    match opcao :
        case 1:
            inserir_placas()
        case 2:
            ler_arquivo()
        case 3:
            atualizar_placas_carros()
        case 4:
            validar_dados_base()
        case 5:
            encerrar_bot()
        case _:
            print('Opção fora do escopo de selção')


def main ():
    selecao = opcoes_menu()


main()