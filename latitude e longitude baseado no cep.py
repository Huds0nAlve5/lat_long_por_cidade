from base64 import encode
from codecs import ignore_errors
import pandas as pd
import pycep_correios as cep
from pycep_correios.exceptions import CEPNotFound, InvalidCEP
from  geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Cidade")
country ="Brazil"

base = pd.read_excel("Cadastro de clientes.xlsx")
lista_base = list(base['CEP'])            #a Serie vira uma lista!
latitude = []
longitude = []

linha = 0

for cp in lista_base:
    try:
        print(cp)
        endereco = cep.get_address_from_cep(cp)
        cidade = endereco['cidade']
        localizacao = geolocator.geocode(cidade + ',' + country)
        base.loc[linha, 'Latitude'] = localizacao.latitude                                      #loc para alocar em determinada linha e coluna
        base.loc[linha, 'Longitude'] = localizacao.longitude
        print('Localizando as latitudes e longitudes! ', linha , ' de ' , len(lista_base))      #encontrar o tamanho de um vetor
        linha = linha + 1
    except InvalidCEP as exc:
        print(exc)

print('Passando as alteracoes para o Excel!')
base.to_excel('Cadastro de clientes.xlsx', index=False) #index false para n impimir a linha no arquivo
print('Sucesso na atualizacao da planilha!')