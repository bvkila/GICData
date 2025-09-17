import pandas as pd

#juntar csv

exportacao = pd.DataFrame()
importacao = pd.DataFrame()

for ano in range(1997, 2025):

    try:
    
        df_exp = pd.read_csv(f"00. DADOS/exportacao/exportacao_{ano}.csv", sep=";", dtype={"CO_ANO": str, "CO_MES": str, "CO_NCM": str, "CO_UNID": str, "CO_PAIS": str, "SG_UF_NCM": str, "CO_VIA": str, "CO_URF": str, "QT_ESTAT": int, "KG_LIQUIDO": int, "VL_FOB": int})
        exportacao = pd.concat([exportacao, df_exp], ignore_index=True) 


        df_imp = pd.read_csv(f"00. DADOS/importacao/importacao_{ano}.csv", sep=";", dtype={"CO_ANO":str, "CO_MES":str, "CO_NCM":str, "CO_UNID":str, "CO_PAIS":str, "SG_UF_NCM":str, "CO_VIA":str, "CO_URF":str, "QT_ESTAT":int, "KG_LIQUIDO":int, "VL_FOB":int, "VL_FRETE":int, "VL_SEGURO":int})
        importacao = pd.concat([importacao, df_imp], ignore_index=True)
    
    except:
        print(f"Erro ao incluir {ano}!")
        pass

exportacao.to_csv("00. DADOS/exportacao/exportacao_1997-2024.csv", index=False, sep=';')
importacao.to_csv("00. DADOS/importacao/importacao_1997-2024.csv", index=False, sep=';')