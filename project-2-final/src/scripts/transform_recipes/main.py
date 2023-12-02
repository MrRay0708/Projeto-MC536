import csv

class Region:
  def __init__(self, id_region, str_region):
    self.id_region = id_region
    self.str_region = str_region

class Category:
  def __init__(self, id_category, str_category, str_category_thumb, str_category_description):
    self.id_category = id_category
    self.str_category = str_category
    self.str_category_thumb = str_category_thumb
    self.str_category_description = str_category_description
    
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


class ProcessedRecipes:
  def __init__(self, recipe: Recipe, category: Category, region: Region) -> None:
    self.id = recipe.id_meal
    self.name = recipe.str_meal
    self.category_id = category.id_category
    self.region_id = region.id_region

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

def format_recipes(recipes, regions, categories):
  p_recipes = []
  
  print("Iniciando transformação das receitas...")
  for recipe in recipes:
    a_category = None
    for category in categories:
      if category.str_category == recipe.str_category:
        a_category = category
        break
      
    if a_category == None: continue
    
    a_region = None
    for region in regions:
      if region.str_region == recipe.str_area:
        a_region = region
        break
      
    if a_region == None: continue
    
    p_recipes.append(ProcessedRecipes(recipe, a_category, a_region))
  
  print("Transformação concluída!")
  
  return p_recipes

def escrever_csv_recipes(list, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    print("Iniciando escrita...")
    
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['id_recipe', 'name_recipe', 'category_id', 'region_id'])

    for item in list:
        escritor_csv.writerow([item.id , item.name, item.category_id, item.region_id])

def main():
  recipes_api= ler_csv('../../../data/external/receitas.csv', Recipe)
  regions_api = ler_csv('../../../data/external/regioes.csv', Region)
  categories_api = ler_csv('../../../data/external/categorias.csv', Category)
  
  p_recipes = format_recipes(recipes_api, regions_api, categories_api)
  
  escrever_csv_recipes(p_recipes, '../../../data/processed/p_recipes.csv')
  
main()