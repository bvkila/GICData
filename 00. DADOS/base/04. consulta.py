import pandas as pd
import sqlite3

caminho = r"C:\Users\joao braga\OneDrive\Documentos\GitHub\GICData\00. DADOS\base\comercio.db"
conn = sqlite3.connect(caminho)

for ano in range(1997, 2026):

    try:

        print(f"Tratando {ano}!")

        url_EXP = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{ano}.csv"
        url_IMP = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_{ano}.csv"

        df_EXP = pd.read_csv(url_EXP, sep=";", dtype=str)
        df_IMP = pd.read_csv(url_IMP, sep=";", dtype=str)

        df = pd.merge(df_EXP, df_IMP, how='outer', on=['CO_ANO','CO_MES', 'CO_NCM', 'CO_UNID', 'CO_PAIS', 'SG_UF_NCM', 'CO_VIA', 'CO_URF'], suffixes=('_EXP', '_IMP'))
        df.to_sql('comercio', conn, if_exists='append', index=False)
        print(df)

    except:
        print(f"Erro ao tratar {ano}!")
        pass


