import pandas as pd

anos = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

consolidado = pd.DataFrame()
erros = []

for ano in anos:
    try:
        print(f"Tratando {ano}")
        url = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_{ano}.csv"
        df = pd.read_csv(url, sep=";", dtype=str)
        consolidado = pd.concat([consolidado, df], ignore_index=True)
        consolidado.to_csv("Importacao.csv", index=False, sep=';')
    except:
        print(f"Erro ao tratar {ano}")
        erros = erros + [ano]
        pass

print('Total de erros: ', erros)