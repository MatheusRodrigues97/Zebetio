import pandas as pd
import csv

COUNT_GLOBAL = 0 

rota = './arquivo/zebetio.xlsx'


def atualizar_dados(lista_feitos):
   with open ('arquivo/log_placas.txt', 'r+') as arquivo:
      for valor in lista_feitos:
         valor = str(valor)
         arquivo.writelines(valor + '\n')

   return 1
   

def arquivo_leitura(x,y):

   df = pd.read_excel(rota)
   value = df[x:y]
   dicioanrio = value.to_dict(orient= 'records')

   return dicioanrio

def arquivo_comparacao(x,y):
   df = pd.read_excel('./arquivo/eletronico072024')
