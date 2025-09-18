import sqlite3
import pandas as pd

caminho = "00. DADOS/base/comercio.db"

conn = sqlite3.connect(caminho)

df = pd.read_sql_query('''
            select * from comercio where CO_ANO in (2023,2024,2025)
''', conn)

print(df)

