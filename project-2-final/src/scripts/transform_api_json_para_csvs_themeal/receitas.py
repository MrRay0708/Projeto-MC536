import csv
import requests

class Recipe:
    def __init__(self, data):
        self.id_meal = data.get("idMeal")
        self.str_meal = data.get("strMeal")
        self.str_drink_alternate = data.get("strDrinkAlternate")
        self.str_category = data.get("strCategory")
        self.str_area = data.get("strArea")
        self.str_instructions = data.get("strInstructions")
        self.str_meal_thumb = data.get("strMealThumb")
        self.str_tags = data.get("strTags")
        self.str_youtube = data.get("strYoutube")
        self.str_ingredient1 = data.get("strIngredient1")
        self.str_ingredient2 = data.get("strIngredient2")
        self.str_ingredient3 = data.get("strIngredient3")
        self.str_ingredient4 = data.get("strIngredient4")
        self.str_ingredient5 = data.get("strIngredient5")
        self.str_ingredient6 = data.get("strIngredient6")
        self.str_ingredient7 = data.get("strIngredient7")
        self.str_ingredient8 = data.get("strIngredient8")
        self.str_ingredient9 = data.get("strIngredient9")
        self.str_ingredient10 = data.get("strIngredient10")
        self.str_ingredient11 = data.get("strIngredient11")
        self.str_ingredient12 = data.get("strIngredient12")
        self.str_ingredient13 = data.get("strIngredient13")
        self.str_ingredient14 = data.get("strIngredient14")
        self.str_ingredient15 = data.get("strIngredient15")
        self.str_ingredient16 = data.get("strIngredient16")
        self.str_ingredient17 = data.get("strIngredient17")
        self.str_ingredient18 = data.get("strIngredient18")
        self.str_ingredient19 = data.get("strIngredient19")
        self.str_ingredient20 = data.get("strIngredient20")
        self.str_measure1 = data.get("strMeasure1")
        self.str_measure2 = data.get("strMeasure2")
        self.str_measure3 = data.get("strMeasure3")
        self.str_measure4 = data.get("strMeasure4")
        self.str_measure5 = data.get("strMeasure5")
        self.str_measure6 = data.get("strMeasure6")
        self.str_measure7 = data.get("strMeasure7")
        self.str_measure8 = data.get("strMeasure8")
        self.str_measure9 = data.get("strMeasure9")
        self.str_measure10 = data.get("strMeasure10")
        self.str_measure11 = data.get("strMeasure11")
        self.str_measure12 = data.get("strMeasure12")
        self.str_measure13 = data.get("strMeasure13")
        self.str_measure14 = data.get("strMeasure14")
        self.str_measure15 = data.get("strMeasure15")
        self.str_measure16 = data.get("strMeasure16")
        self.str_measure17 = data.get("strMeasure17")
        self.str_measure18 = data.get("strMeasure18")
        self.str_measure19 = data.get("strMeasure19")
        self.str_measure20 = data.get("strMeasure20")
        self.str_source = data.get("strSource")
        self.str_image_source = data.get("strImageSource")
        self.str_creative_commons_confirmed = data.get("strCreativeCommonsConfirmed")
        self.date_modified = data.get("dateModified")


def obter_lista_receitas(letra):
  url = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + letra

  resposta = requests.get(url)

  if resposta.status_code == 200:
    dados_json = resposta.json()

    receitas_json = dados_json.get("meals", [])

    lista_receitas = []
    if(receitas_json):
      lista_receitas = [
        Recipe(
          receita
        )
        for receita in receitas_json
      ]

    return lista_receitas
  else:
    print(f"Erro na requisição. Código de status: {resposta.status_code}")
    return None
    

def escrever_csv(lista_recipes, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow([
      'IdMeal', 'StrMeal', 'StrDrinkAlternate', 'StrCategory', 'StrArea',
      'StrInstructions', 'StrMealThumb', 'StrTags', 'StrYoutube',
      'StrIngredient1', 'StrIngredient2', 'StrIngredient3', 'StrIngredient4',
      'StrIngredient5', 'StrIngredient6', 'StrIngredient7', 'StrIngredient8',
      'StrIngredient9', 'StrIngredient10', 'StrIngredient11', 'StrIngredient12',
      'StrIngredient13', 'StrIngredient14', 'StrIngredient15', 'StrIngredient16',
      'StrIngredient17', 'StrIngredient18', 'StrIngredient19', 'StrIngredient20',
      'StrMeasure1', 'StrMeasure2', 'StrMeasure3', 'StrMeasure4', 'StrMeasure5',
      'StrMeasure6', 'StrMeasure7', 'StrMeasure8', 'StrMeasure9', 'StrMeasure10',
      'StrMeasure11', 'StrMeasure12', 'StrMeasure13', 'StrMeasure14', 'StrMeasure15',
      'StrMeasure16', 'StrMeasure17', 'StrMeasure18', 'StrMeasure19', 'StrMeasure20',
      'StrSource', 'StrImageSource', 'StrCreativeCommonsConfirmed', 'DateModified'
    ])

    for recipe in lista_recipes:
      escritor_csv.writerow([
        recipe.id_meal, recipe.str_meal, recipe.str_drink_alternate, recipe.str_category,
        recipe.str_area, recipe.str_instructions, recipe.str_meal_thumb, recipe.str_tags,
        recipe.str_youtube, recipe.str_ingredient1, recipe.str_ingredient2, recipe.str_ingredient3,
        recipe.str_ingredient4, recipe.str_ingredient5, recipe.str_ingredient6, recipe.str_ingredient7,
        recipe.str_ingredient8, recipe.str_ingredient9, recipe.str_ingredient10, recipe.str_ingredient11,
        recipe.str_ingredient12, recipe.str_ingredient13, recipe.str_ingredient14, recipe.str_ingredient15,
        recipe.str_ingredient16, recipe.str_ingredient17, recipe.str_ingredient18, recipe.str_ingredient19,
        recipe.str_ingredient20, recipe.str_measure1, recipe.str_measure2, recipe.str_measure3,
        recipe.str_measure4, recipe.str_measure5, recipe.str_measure6, recipe.str_measure7,
        recipe.str_measure8, recipe.str_measure9, recipe.str_measure10, recipe.str_measure11,
        recipe.str_measure12, recipe.str_measure13, recipe.str_measure14, recipe.str_measure15,
        recipe.str_measure16, recipe.str_measure17, recipe.str_measure18, recipe.str_measure19,
        recipe.str_measure20, recipe.str_source, recipe.str_image_source,
        recipe.str_creative_commons_confirmed, recipe.date_modified
      ])
        

def main():

  alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  lista_receitas = []
  for letra in alfabeto:
    print(letra)
    result = obter_lista_receitas(letra)

    if(result):
      lista_receitas += result

  if lista_receitas:
    escrever_csv(lista_receitas, '../../../data/external/receitas.csv') 
      

main()