import pandas as pd
import sqlite3

caminho = r"00. DADOS\base\GICData.db"
conn = sqlite3.connect(caminho)
cursor = conn.cursor()

ano = input("Digite o ano que deseja incluir na base: ")

try:

    print(f"Tratando {ano}!")

    url_EXP = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{ano}.csv"
    url_IMP = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_{ano}.csv"

    df_EXP = pd.read_csv(url_EXP, sep=";", dtype=str)
    df_EXP = df_EXP.groupby(['CO_ANO','CO_MES', 'CO_NCM', 'CO_UNID', 'CO_PAIS', 'SG_UF_NCM','CO_VIA', 'CO_URF']).agg({'QT_ESTAT':'sum', 'KG_LIQUIDO':'sum', 'VL_FOB':'sum'})

    df_IMP = pd.read_csv(url_IMP, sep=";", dtype=str)
    df_IMP = df_IMP.groupby(['CO_ANO','CO_MES', 'CO_NCM', 'CO_UNID', 'CO_PAIS', 'SG_UF_NCM', 'CO_VIA', 'CO_URF']).agg({'QT_ESTAT':'sum', 'KG_LIQUIDO':'sum', 'VL_FOB':'sum', 'VL_FRETE':'sum', 'VL_SEGURO':'sum'})
    df_IMP = df_IMP.rename(columns={'VL_FRETE':'VL_FRETE_IMP', 'VL_SEGURO':'VL_SEGURO_IMP'})

    df = pd.merge(df_EXP, df_IMP, how='outer', on=['CO_ANO','CO_MES', 'CO_NCM', 'CO_UNID', 'CO_PAIS', 'SG_UF_NCM', 'CO_VIA', 'CO_URF'], suffixes=('_EXP', '_IMP'))
    df = df.reset_index()

    cursor.execute("delete from comercio where CO_ANO = ?", (ano))
    conn.commit()

    df.to_sql('comercio', conn, if_exists='append', index=False)
    
    print(df)
    
    print(f'Ano {ano} concluído!')

except:
    print(f"Erro ao tratar {ano}!")
    pass