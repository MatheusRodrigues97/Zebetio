import pyautogui as py
import time
import pyperclip as clip
import datetime 

py.PAUSE = 0.50

def validador_dados(status):
    '''
    Validar o dados da guia com base do status do sistema
    '''
    if status == 'estoque' or status == 'pendente de analise':
        return True
    else:
        return False


def mover(posicao):
    '''
    posição passada
    '''
    px , pz =posicao
    time.sleep(0.75)
    py.moveTo(x= px,y= pz,duration= 0.5)
    py.click(x= px,y= pz)
    time.sleep(2)

    return 1

def escrever_dados(value):
    '''
    Escrever dados na posição passada
    '''
    if value:
        py.write(value,interval= 0.25)
        time.sleep(3.50)
        py.press('esc')
    else:
        py.alert(text = 'Dados erro', title = 'Erro', button= 'OK')
    
    return 1

    


def placa(placa):
    '''
    Adicioanr placa e status no carro 
    '''
    retorno = 0
    posicao01= (277,379)
    posicao02= (197,442)
    posicao03= (204,432)

    if retorno == 0:
        mover(posicao01)
        mover(posicao02)
        py.click(posicao02, clicks=2)
        escrever_dados(placa)
        mover(posicao03)
        py.press('esc')
        retorno = 1
    else:
        py.alert(text = 'Função repetida', title = 'Erro', button= 'OK')
    return retorno
        
def debito(debito):
    '''
    Inserir e validadar dados
    '''
    posicao01 = (227,526)
    posicao02 = (168,588) 
    posicao03 = (390,592) 

    mover(posicao01)
    mover(posicao02)
    py.click(posicao02, clicks=2)
    debito = str(debito)
    escrever_dados(debito)
    mover(posicao03)
    time.sleep(2.5)
    py.press('enter')
    
    return 1 

def validar_debito(dados):
    '''
    Função para validar dados do debito    
    '''
    
    py.press('right',presses=5)
    py.hotkey('ctrl', 'c')
    value = clip.paste()

    if validador_dados(value):

        for indice, valor in dados.items():
            
            match indice:
                
                case 'placa':
                    
                    py.press('left', presses= 5)
                    placa = valor
                    escrever_dados(valor)

                case 'valor':

                    py.press('right', presses= 2)
                    clip.copy(valor)
                    py.hotkey('ctrl', 'v')

                case 'data de inscricao':

                    py.press('right', presses= 1)
                    valor_formatado = datetime.date.strftime(valor, '%m-%d-%Y')
                    clip.copy(valor_formatado)
                    py.hotkey('ctrl', 'v')
                    valor = valor_formatado

                
                case 'vencimento':

                    py.press('right', presses= 1)
                    valor_formatado = datetime.date.strftime(valor, '%m-%d-%Y')
                    clip.copy(valor_formatado)
                    py.hotkey('ctrl', 'v')
                    valor = valor_formatado

                
                case 'feito':

                    py.press('left', presses=6)
                    py.press('enter')
                    py.write(placa,interval=0.5)
                    time.sleep(3)
                    py.press('enter')
                    py.press('esc')
                    time.sleep(0.50)
                    py.press('esc', presses= 2)
                    valor = 'SIM'
                
                case 'repetido':
                    valor = 'N'

    else:
        for index, valor in dados.items():
            match index :
                case 'placa':
                    placa = valor

                case 'repetido':
                    valor = 'S'
                    
                case 'feito':
                    py.press('left', presses=6)
                    py.press('enter')
                    py.write(placa,interval=0.5)
                    time.sleep(3)
                    py.press('enter')
                    py.press('esc')
                    time.sleep(0.50)
                    py.press('esc', presses= 2)
                    valor = 'SIM'
        return dados

    return dados
            





    
     


    






        



    

    