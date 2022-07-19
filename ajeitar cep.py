from ctypes import sizeof
import pandas as pd

base = pd.read_excel("Cadastro de clientes.xlsx")
lista_base = list(base['CEP'])           #a Serie vira uma lista!
cep_corrigido = []
x = 0

for cp in lista_base:
    cepp = str(cp)
    if(str(cp) != 'fim'):
        print(cp)
        cep_corrigido.append(cepp[0:5] + "-" + cepp[5:8])
    else:
        break

base['CEP'] = cep_corrigido

base.to_excel("Cadastro de clientes.xlsx", index=False)