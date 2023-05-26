import os
import pandas as pd
from openpyxl.styles import numbers
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from gerar import gerarTxt
def extrair_dados_csv(csv_file):

    df = pd.read_csv(csv_file, header=None, sep=';', encoding='latin-1')
    df.columns = df.iloc[0]
    df = df[1:]
    ordem_colunas = ['LINHA_NUM','TOMA_CPF_CGC','6336','SP','ENFS_DAT_ESCRITURACAO','ENFS_NUM_NFS_INI','ENFS_NUM_NFS_FIM','SR','', 'VALOR_FATURADO','BASE_CALC','','','','','','','V','','','','','','','','','','','','','','','','','','','','','','','','','','',"R","","","","SVTB_COD_SERVICO"]
    print(len(ordem_colunas))
    df_novo = pd.DataFrame(columns=ordem_colunas)

    for coluna in df_novo.columns:
        if coluna in df.columns:
            if coluna == 'ENFS_DAT_ESCRITURACAO':
               datas_convertidas = []            
               for linha in df[coluna]:
                   dia, mes, ano = linha.split("/")
                   data_formatada = f"{ano}/{mes}/{dia}"
                   datas_convertidas.append(data_formatada)
               df_novo[coluna] = datas_convertidas
            else:
               df_novo[coluna] = df[coluna].astype(str)
        elif coluna == 'R':
            df_novo[coluna] = 'R'
        elif coluna == 'V':
            df_novo[coluna] = 'V'
        elif coluna == "6336":
            df_novo[coluna] = '6336'
        elif coluna == "SP":
            df_novo[coluna] = 'SP'
        else:
            df_novo[coluna] = ''
    wb = Workbook()
    ws = wb.active
    for row in dataframe_to_rows(df_novo, index=False, header=True):
        ws.append(row)
    data_column_index = ordem_colunas.index('ENFS_DAT_ESCRITURACAO') + 1 
    data_column_letter = chr(data_column_index + 64) 
    for cell in ws[data_column_letter]:
        cell.number_format = numbers.FORMAT_DATE_YYYYMMDD2
    print(df_novo['ENFS_DAT_ESCRITURACAO'])
    diretorio = './dados'
    if not os.path.exists(diretorio):
       os.makedirs(diretorio)
    caminho_arquivo = os.path.join(diretorio,'dados_formatados.xlsx')
    wb.save(caminho_arquivo)
    
    
   
    
    
    

csv_file = './dados/BRUTO.csv'

dados_por_coluna = extrair_dados_csv(csv_file)

print(dados_por_coluna)

gerarTxt()
