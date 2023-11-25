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

  # Faz a requisição HTTP
  resposta = requests.get(url)

  # Verifica se a requisição foi bem-sucedida (código de status 200)
  if resposta.status_code == 200:
    # Converte os dados JSON para um dicionário Python
    dados_json = resposta.json()

    # Obtém a lista de ingredientes
    ingredientes_json = dados_json.get("meals", [])

    # Cria objetos Ingredient a partir dos dados JSON
    lista_ingredientes = [
      Ingredient(
        ingrediente.get("idIngredient"),
        ingrediente.get("strIngredient"),
        ingrediente.get("strDescription"),
        ingrediente.get("strType")
      )
      for ingrediente in ingredientes_json
    ]

    # Retorna a lista de ingredientes
    return lista_ingredientes
  else:
      # Se a requisição não foi bem-sucedida, imprime uma mensagem de erro
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