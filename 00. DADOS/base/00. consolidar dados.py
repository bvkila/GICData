import pandas as pd

variavel = 1

if variavel == 1:
    tipo_url = 'EXP'
    tipo_pasta = 'exportacao'

if variavel == 2:
    tipo_url = 'IMP'
    tipo_pasta = 'importacao'


for ano in range(1997, 2026):

    try:

        print(f"Tratando {ano}!")

        url = f"https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/{tipo_url}_{ano}.csv"

        df = pd.read_csv(url, sep=";", dtype=str)
        df.to_csv(f"00. DADOS/{tipo_pasta}/{tipo_pasta}_{ano}.csv", index=False, sep=';')

        print(f"Finalizado {ano}!")

    except:
        print(f"Erro ao tratar {ano}!")
        pass
