import sqlite3
import pandas as pd

caminho = r"00. DADOS\base\comercio.db"
conn = sqlite3.connect(caminho)

df = pd.read_sql_query('''
                        SELECT
                            CO_ANO,
                            CO_MES,
                            SUBSTR(CO_NCM, 1, 2) AS capitulo,
                            CO_PAIS,
                            SUM(VL_FOB_EXP) AS exportacoes

                        FROM
                            comercio

                        GROUP BY
                            CO_ANO,
                            CO_MES,
                            SUBSTR(CO_NCM, 1, 2),
                            CO_PAIS
                            
                        HAVING
                            exportacoes > 0
                       ''', conn)

print(df)
df.to_excel('dados_Marta.xlsx', index=False)