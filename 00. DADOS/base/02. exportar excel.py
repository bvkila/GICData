import sqlite3
import pandas as pd

caminho = r"00. DADOS\base\GICData.db"
conn = sqlite3.connect(caminho)

df = pd.read_sql_query('''
    SELECT
        c.CO_ANO,
        c.CO_MES,
        SUBSTR(c.CO_NCM, 1, 2) AS capitulo,
        tp."PAIS.NOME" AS nome_pais,
        SUM(c.VL_FOB_EXP) AS exportacoes
    FROM
        comercio AS c
    LEFT JOIN
        tradutor_pais AS tp ON c.CO_PAIS = tp.CO_PAIS
    WHERE
        c.CO_ANO IN (2023, 2024, 2025)
    GROUP BY
        c.CO_ANO,
        c.CO_MES,
        SUBSTR(c.CO_NCM, 1, 2),
        tp."PAIS.NOME"
    HAVING
        exportacoes > 0;
                       ''', conn)

print(df)
df.to_excel('dados_19.09.xlsx', index=False)