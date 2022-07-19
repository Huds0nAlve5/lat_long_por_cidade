from base64 import encode
from codecs import ignore_errors
from multiprocessing.connection import wait
from time import sleep
import pandas as pd
import pycep_correios as cep
from pycep_correios import exceptions
from  geopy.geocoders import Nominatim
from pycep_correios import WebService

geolocator = Nominatim(user_agent="Cidade")
country ="Brazil"
estado = "Ceará"

base = pd.read_excel("Cadastro de clientes.xlsx")
lista_cidades = list(base['Cidade'])            #a Serie vira uma lista!
latitude = []
longitude = []

linha = 0

for city in lista_cidades:
    print(city)
    localizacao = geolocator.geocode(city + ',' + estado + ',' + country)
    base.loc[linha, 'Latitude'] = localizacao.latitude                                      #loc para alocar em determinada linha e coluna
    base.loc[linha, 'Longitude'] = localizacao.longitude
    print('Localizando as latitudes e longitudes! ', linha , ' de ' , len(lista_cidades))      #encontrar o tamanho de um vetor
    linha = linha + 1

print('Passando as alteracoes para o Excel!')
base.to_excel('Cadastro de clientes.xlsx', index=False) #index false para n impimir a linha no arquivo
print('Sucesso na atualizacao da planilha!')