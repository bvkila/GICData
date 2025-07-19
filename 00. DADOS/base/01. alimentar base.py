import sqlite3
import pandas as pd
import time

caminho = "00. DADOS/base/comercio.db"

conn = sqlite3.connect(caminho)

for ano in range(1997, 2026):

    try:
    
        df = pd.read_csv(f"00. DADOS/exportacao/exportacao_{ano}.csv", sep=";", dtype={"CO_ANO": str, "CO_MES": str, "CO_NCM": str, "CO_UNID": str, "CO_PAIS": str, "SG_UF_NCM": str, "CO_VIA": str, "CO_URF": str, "QT_ESTAT": int, "KG_LIQUIDO": int, "VL_FOB": int})
        df.to_sql('exportacao', conn, if_exists='append', index=False)

        df = pd.read_csv(f"00. DADOS/importacao/importacao_{ano}.csv", sep=";", dtype={"CO_ANO":str, "CO_MES":str, "CO_NCM":str, "CO_UNID":str, "CO_PAIS":str, "SG_UF_NCM":str, "CO_VIA":str, "CO_URF":str, "QT_ESTAT":int, "KG_LIQUIDO":int, "VL_FOB":int, "VL_FRETE":int, "VL_SEGURO":int})
        df.to_sql('importacao', conn, if_exists='append', index=False)

        time.sleep(5)

        print(f"Finalizado {ano}!")

    except:
        print(f"Erro ao incluir {ano}!")
        pass