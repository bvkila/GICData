import sqlite3
import pandas as pd

caminho = "00. DADOS/base/comercio.db"

conn = sqlite3.connect(caminho)
cursor = conn.cursor()

ano = 2025

for i in {1,2}:
    
    variavel = i

    if variavel == 1:
        tipo_url = 'EXP'
        tipo = 'exportacao'

    if variavel == 2:
        tipo_url = 'IMP'
        tipo = 'importacao'

    try:

        print(f"Tratando {ano}!")

        url = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/{tipo_url}_{ano}.csv"

        delete = cursor.execute(f'''
                                DELETE FROM {tipo} WHERE CO_ANO = '{ano}'
                                ''')
        conn.commit()

        print(f"Deletado {ano} para {tipo}!")

        df = pd.read_csv(url, sep=";", dtype={"CO_ANO": str, "CO_MES": str, "CO_NCM": str, "CO_UNID": str, "CO_PAIS": str, "SG_UF_NCM": str, "CO_VIA": str, "CO_URF": str, "QT_ESTAT": int, "KG_LIQUIDO": int, "VL_FOB": int})
        df.to_sql(f'{tipo}', conn, if_exists='append', index=False)

        print(f"Finalizado {ano} para {tipo}!")

    except:
        print(f"Erro ao tratar {ano} para {tipo}!")
        pass