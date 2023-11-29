import csv
import requests

class Category:
  def __init__(self, id_category, str_category, str_category_thumb, str_category_description):
    self.id_category = id_category
    self.str_category = str_category
    self.str_category_thumb = str_category_thumb
    self.str_category_description = str_category_description

def obter_lista_categorias():
  url = "https://www.themealdb.com/api/json/v1/1/categories.php"

  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados_json = resposta.json()

    categorias_json = dados_json.get("categories", [])

    lista_categorias = [
      Category(
        categoria.get("idCategory"),
        categoria.get("strCategory"),
        categoria.get("strCategoryThumb"),
        categoria.get("strCategoryDescription")
      )
      for categoria in categorias_json
    ]

    return lista_categorias
  else:
    print(f"Erro na requisição. Código de status: {resposta.status_code}")
    return None
    

def escrever_csv(lista_categorias, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['Id', 'Name', 'Thumb', 'Description'])

    for categoria in lista_categorias:
      escritor_csv.writerow([categoria.id_category, categoria.str_category, categoria.str_category_thumb, categoria.str_category_description])
        

def main():

  lista_categorias = obter_lista_categorias()
  if lista_categorias:
    escrever_csv(lista_categorias, '../../../data/external/categorias.csv') 
      

main()