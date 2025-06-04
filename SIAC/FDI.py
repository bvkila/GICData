import pandas as pd

df = pd.read_csv('FDI.csv', sep=',', dtype=str)
df = df[['COUNTRY', 'COUNTERPART_COUNTRY','INDICATOR','2009','2019','2023']]

FDIChina = df[df['COUNTRY'] == "China, People's Republic of"]
print(FDIChina)

FDIEUA = df[df['COUNTRY'] == 'United States']
print(FDIEUA)