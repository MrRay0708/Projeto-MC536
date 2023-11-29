import csv
import requests

class Region:
  def __init__(self, id_region, str_region):
    self.id_region = id_region
    self.str_region = str_region

def obter_lista_regioes():
  url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"

  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados_json = resposta.json()

    regiao_json = dados_json.get("meals", [])

    lista_regioes = [
      Region(
        i + 1,
        regiao_json[i].get("strArea"),
      )
      for i in range(len(regiao_json))
    ]

    return lista_regioes
  else:
    print(f"Erro na requisição. Código de status: {resposta.status_code}")
    return None
    

def escrever_csv(lista_regioes, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['Id', 'Name'])

    for regiao in lista_regioes:
      escritor_csv.writerow([regiao.id_region, regiao.str_region])
        

def main():

  lista_regioes = obter_lista_regioes()
  if lista_regioes:
    escrever_csv(lista_regioes, '../../../data/external/regioes.csv') 
      

main()