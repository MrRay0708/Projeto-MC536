import csv

class Recipe:
  def __init__(self, idMeal, strMeal, strDrinkAlternate, strCategory, strArea, strInstructions, strMealThumb, strTags, strYoutube, 
               strIngredient1, strIngredient2, strIngredient3, strIngredient4, strIngredient5, strIngredient6, strIngredient7, strIngredient8,
               strIngredient9, strIngredient10, strIngredient11, strIngredient12, strIngredient13, strIngredient14, strIngredient15, strIngredient16, 
               strIngredient17, strIngredient18, strIngredient19, strIngredient20, strMeasure1, strMeasure2, strMeasure3, strMeasure4, 
               strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10, strMeasure11, strMeasure12, 
               strMeasure13, strMeasure14, strMeasure15, strMeasure16, strMeasure17, strMeasure18, strMeasure19, strMeasure20,
               strSource, strImageSource, strCreativeCommonsConfirmed, dateModified
  ):
    self.id_meal = idMeal
    self.str_meal = strMeal
    self.str_drink_alternate = strDrinkAlternate
    self.str_category = strCategory
    self.str_area = strArea
    self.str_instructions = strInstructions
    self.str_meal_thumb = strMealThumb
    self.str_tags = strTags
    self.str_youtube = strYoutube
    self.str_ingredient1 = strIngredient1
    self.str_ingredient2 = strIngredient2
    self.str_ingredient3 = strIngredient3
    self.str_ingredient4 = strIngredient4
    self.str_ingredient5 = strIngredient5
    self.str_ingredient6 = strIngredient6
    self.str_ingredient7 = strIngredient7
    self.str_ingredient8 = strIngredient8
    self.str_ingredient9 = strIngredient9
    self.str_ingredient10 = strIngredient10
    self.str_ingredient11 = strIngredient11
    self.str_ingredient12 = strIngredient12
    self.str_ingredient13 = strIngredient13
    self.str_ingredient14 = strIngredient14
    self.str_ingredient15 = strIngredient15
    self.str_ingredient16 = strIngredient16
    self.str_ingredient17 = strIngredient17
    self.str_ingredient18 = strIngredient18
    self.str_ingredient19 = strIngredient19
    self.str_ingredient20 = strIngredient20
    self.str_measure1 = strMeasure1
    self.str_measure2 = strMeasure2
    self.str_measure3 = strMeasure3
    self.str_measure4 = strMeasure4
    self.str_measure5 = strMeasure5
    self.str_measure6 = strMeasure6
    self.str_measure7 = strMeasure7
    self.str_measure8 = strMeasure8
    self.str_measure9 = strMeasure9
    self.str_measure10 = strMeasure10
    self.str_measure11 = strMeasure11
    self.str_measure12 = strMeasure12
    self.str_measure13 = strMeasure13
    self.str_measure14 = strMeasure14
    self.str_measure15 = strMeasure15
    self.str_measure16 = strMeasure16
    self.str_measure17 = strMeasure17
    self.str_measure18 = strMeasure18
    self.str_measure19 = strMeasure19
    self.str_measure20 = strMeasure20
    self.str_source = strSource
    self.str_image_source = strImageSource
    self.str_creative_commons_confirmed = strCreativeCommonsConfirmed
    self.date_modified = dateModified


class Ingredient:
    def __init__(self, id_ingredient, str_ingredient, str_description, str_type):
      self.id_ingredient = id_ingredient
      self.str_ingredient = str_ingredient
      self.str_description = str_description
      self.str_type = str_type
      
class IngredientRecipe:
  def __init__(self, ingredient: Ingredient, recipe: Recipe, qtde) -> None:
    self.ingredient_id = ingredient.id_ingredient
    self.recipe_id = recipe.id_meal
    self.qtde = qtde

def ler_csv(nome_arquivo, from_class):
  lista_objetos = []

  k = 0
  with open(nome_arquivo, 'r', encoding="utf8") as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)

      next(leitor_csv, None)

      for linha in leitor_csv:
        # Cria objeto do food que sera armazenado na lista
        food = from_class(*linha)
      
        lista_objetos.append(food)

  return lista_objetos


def format_ingredients_recipes(recipes, ingridients):
  print("Iniciando transformação...")
  
  p_ingredients_recipes = []
  
  for recipe in recipes:
    for i in range(1,21):
      for ingredient in ingridients:
        if ingredient.str_ingredient == getattr(recipe, f"str_ingredient{i}"):
          p_ingredients_recipes.append(IngredientRecipe(ingredient, recipe, getattr(recipe, f"str_measure{i}")))
          break
        
  return p_ingredients_recipes

def escrever_csv_recipes(list, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    print("Iniciando escrita...")
    
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['id_ingredient', 'id_recipe', 'qtde'])

    for item in list:
        escritor_csv.writerow([item.ingredient_id , item.recipe_id, item.qtde])
        
  print("Processo Finalizado.")

def main():
  recipes_api = ler_csv('../../../data/external/receitas.csv', Recipe)
  ingredients_processed = ler_csv('../../../data/processed/p_ingredients.csv', Ingredient)
  
  p_ingredients_recipes = format_ingredients_recipes(recipes_api, ingredients_processed)
  
  escrever_csv_recipes(p_ingredients_recipes, '../../../data/processed/p_ingredients_recipes.csv')
  
main()