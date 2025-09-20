# import pandas as pd
# import sqlite3

# conn = sqlite3.connect(r"00. DADOS\base\GICData.db")
# caminho_tradutores = r"00. DADOS\base\tradutores.xlsx"

# tradPais = pd.read_excel(caminho_tradutores, sheet_name="TRAD.CO_PAIS", dtype=str)
# tradNCM = pd.read_excel(caminho_tradutores, sheet_name="TRAD.CO_NCM", dtype=str)

# tradPais.to_sql('tradutor_pais', conn, if_exists='replace', index=False)
# tradNCM.to_sql('tradutor_ncm', conn, if_exists='replace', index=False)
