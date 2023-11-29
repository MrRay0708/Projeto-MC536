import csv
import requests

class Ingredient:
  def __init__(self, id_ingredient, str_ingredient, str_description, str_type):
    self.id_ingredient = id_ingredient
    self.str_ingredient = str_ingredient
    self.str_description = str_description
    self.str_type = str_type
      
def obter_lista_ingredientes():
  url = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"

  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados_json = resposta.json()

    ingredientes_json = dados_json.get("meals", [])

    lista_ingredientes = [
      Ingredient(
        ingrediente.get("idIngredient"),
        ingrediente.get("strIngredient"),
        ingrediente.get("strDescription"),
        ingrediente.get("strType")
      )
      for ingrediente in ingredientes_json
    ]

    return lista_ingredientes
  else:
    print(f"Erro na requisição. Código de status: {resposta.status_code}")
    return None
      
def escrever_csv(lista_ingredientes, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['ID', 'Nome', 'Descrição', 'Tipo'])

    for ingrediente in lista_ingredientes:
      escritor_csv.writerow([ingrediente.id_ingredient, ingrediente.str_ingredient, ingrediente.str_description, ingrediente.str_type])
        
def main():
  lista_ingredientes = obter_lista_ingredientes()

  if lista_ingredientes:
    escrever_csv(lista_ingredientes, '../../../data/external/ingredientes.csv') 
      
main()