import pandas as pd
import os
def gerarTxt():
    
# Ler arquivo XLSX
    df = pd.read_excel('./dados/dados_formatados.xlsx')
    diretorio = './dados'
    caminho_arquivo = os.path.join(diretorio,'dados.txt')
    # Criar arquivo TXT
    with open(caminho_arquivo, 'w') as txt_file:
        # Iterar sobre as linhas do DataFrame
        for _, row in df.iterrows():
            # Verificar se a linha possui 46 campos
            print(len(row))
            if len(row) == 49:
                # Criar lista com os campos que serão utilizados
                campos = []
                for index,campo in enumerate(row):
                    if pd.notnull(campo):
                        if index == 4:
                           ano, mes, dia = campo.split('/')
                           data_formatada = f"{ano}{mes}{dia}"
                           campos.append(str(data_formatada)) 
                           continue
                        if type(campo) == str:
                           campo_formatado = f'"{campo}"'
                           campos.append(str(campo_formatado))
                        else:
                           campos.append(str(campo))
                    else:
                        campos.append("")

                # Converter lista em string separada por vírgulas
                linha = ",".join(campos)

                # Escrever linha no arquivo TXT
                txt_file.write(linha + '\n')

    # Imprimir número de linhas criadas
    print(f'Foram criadas {len(df)} linhas no arquivo TXT.')

__all__ = ['gerarTxt']