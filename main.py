import os
LINHA = '*'*30


def inserir_placas():
    pass

def ler_arquivo():
    pass

def atualizar_placas_carros():
    pass

def validar_dados_base():
    pass

def encerrar_bot():
    pass

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

    opcao = int(input('\nDigite a opção desejada :'))

    return opcao


def main ():
    opcoes_menu()


main()