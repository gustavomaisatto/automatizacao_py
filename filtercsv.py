import os
import pandas as pd
from openpyxl.styles import numbers
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
from gerar import gerarTxt
def extrair_dados_csv(csv_file):

    # Ler o arquivo CSV com o pandas
    df = pd.read_csv(csv_file, header=None, sep=';', encoding='latin-1')
    df.columns = df.iloc[0]
    df = df[1:]
    ordem_colunas = ['LINHA_NUM','TOMA_CPF_CGC','6336','SP','ENFS_DAT_ESCRITURACAO','ENFS_NUM_NFS_INI','ENFS_NUM_NFS_FIM','SR','', 'VALOR_FATURADO','BASE_CALC','','','','','','','V','','','','','','','','','','','','','','','','','','','','','','','','','','',"R","","","","SVTB_COD_SERVICO"]
    print(len(ordem_colunas))
    # Criar um novo DataFrame vazio com as colunas na ordem desejada
    df_novo = pd.DataFrame(columns=ordem_colunas)

# Preencher o novo DataFrame com os dados do DataFrame original, substituindo-os por strings vazias nas colunas correspondentes
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
    # Criar um arquivo Excel usando o openpyxl
    wb = Workbook()
    ws = wb.active
    for row in dataframe_to_rows(df_novo, index=False, header=True):
        ws.append(row)
    data_column_index = ordem_colunas.index('ENFS_DAT_ESCRITURACAO') + 1  # Adicione +1 porque a indexação das colunas no Excel começa em 1
    data_column_letter = chr(data_column_index + 64)  # Convertendo o índice da coluna para a letra da coluna
    for cell in ws[data_column_letter]:
        cell.number_format = numbers.FORMAT_DATE_YYYYMMDD2  # Definir o formato da célula como 'DD/MM/AAAA'
    # df_novo['ENFS_DAT_ESCRITURACAO'] = pd.to_datetime(df_novo['ENFS_DAT_ESCRITURACAO'], format='%d/%m/%Y')
    # df_novo['ENFS_DAT_ESCRITURACAO'] = df_novo['ENFS_DAT_ESCRITURACAO'].dt.strftime('%Y/%m/%d')
    print(df_novo['ENFS_DAT_ESCRITURACAO'])
# Preencher o DataFrame com os dados do DataFrame transposto
    diretorio = './dados'
    if not os.path.exists(diretorio):
       os.makedirs(diretorio)
    caminho_arquivo = os.path.join(diretorio,'dados_formatados.xlsx')
    wb.save(caminho_arquivo)
    
    
   
    
    
    # Extrair os dados por coluna
    

# Exemplo de arquivo CSV de entrada
csv_file = './dados/BRUTO.csv'

# Extrair os dados por coluna do CSV
dados_por_coluna = extrair_dados_csv(csv_file)

# Exemplo de acesso aos dados
print(dados_por_coluna)

gerarTxt()

# def converter_csv_para_json(csv_file, json_file):
#     # Abrir o arquivo CSV de entrada
#     dados = []
#     # Abrir o arquivo CSV de entrada
#     with open(csv_file, 'r') as arquivo_csv:
#         leitor_csv = csv.DictReader(arquivo_csv)
#         # Ler cada linha do CSV
#         for linha in leitor_csv:
#             dados.append(linha)
#     # Escrever os dados do CSV em um arquivo JSON
#     with open(json_file, 'w') as arquivo_json:
#         json.dump(dados, arquivo_json, indent=4)


# # Exemplo de arquivo CSV de entrada
# csv_file = 'BRUTO.csv'

# # Nome do arquivo JSON de saída
# json_file = 'dados.json'

# def converter_json_para_csv(json_file, csv_file):
#     # Abrir o arquivo JSON de entrada
#     with open(json_file, 'r') as arquivo_json:
#         dados = json.load(arquivo_json)

#     # Obter todas as chaves dos registros
#     chaves = set()
#     for registro in dados:
#         chaves.update(registro.keys())


#     # Abrir o arquivo CSV de saída
#     with open(csv_file, 'w', newline='') as arquivo_csv:
#         escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=list(chaves))

#         # Escrever o cabeçalho
#         escritor_csv.writeheader()

#         # Escrever os registros
#         escritor_csv.writerows(dados)

# # Exemplo de arquivo JSON de entrada
# jsonconvert_file = 'dados.json'

# # Nome do arquivo CSV de saída
# csvconvert_file = 'dadosfiltered.csv'

# # Converter CSV para JSON
# converter_csv_para_json(csv_file, json_file)

# # Converter JSON para CSV
# converter_json_para_csv(jsonconvert_file, csvconvert_file)