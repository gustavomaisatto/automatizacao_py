import pandas as pd
import os
def gerarTxt():
    
    df = pd.read_excel('./dados/dados_formatados.xlsx')
    diretorio = './dados'
    caminho_arquivo = os.path.join(diretorio,'dados.txt')
    with open(caminho_arquivo, 'w') as txt_file:
        for _, row in df.iterrows():
            print(len(row))
            if len(row) == 49:
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

                linha = ",".join(campos)

                txt_file.write(linha + '\n')

    print(f'Foram criadas {len(df)} linhas no arquivo TXT.')

__all__ = ['gerarTxt']