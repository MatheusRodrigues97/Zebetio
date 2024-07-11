import pyautogui as py
from auxiliar import adicionar,arquivo



def main(intervalo):
    py.confirm(text='Analise zebetio', title='Zebetio', buttons=['Iniciar', 'Cancelar'])
    
    inicio = 0
    fim = inicio + intervalo
    
    dicioanrios_dados = arquivo.arquivo_leitura(inicio, fim)
    lista_placas_feitas = [ ]

    for value in dicioanrios_dados:

        for index, valor in value.items():

            match index:

                case 'placa':

                    retorno = adicionar.placa(valor)
                    if not retorno == 1 : break

                case 'notificacao':

                    retorno = adicionar.debito(valor)
                    if retorno == 1:
                        retorno = adicionar.validar_debito(value)
        lista_placas_feitas.append(retorno)    
    
    arquivo.atualizar_dados(lista_placas_feitas)
                            
              
main(500)

'''py.displayMousePosition()'''

