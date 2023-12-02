import csv
    
class FoodData:
  def __init__(self, id, source_id, source_type, food_id, orig_food_id, orig_food_common_name, orig_food_scientific_name, orig_food_part, orig_source_id, orig_source_name, orig_content, orig_min, orig_max, orig_unit, orig_citation, citation, citation_type, creator_id, updater_id, created_at, updated_at, orig_method, orig_unit_expression, standard_content, preparation_type, export):
    self.id = id
    self.source_id = source_id
    self.source_type = source_type
    self.food_id = food_id
    self.orig_food_id = orig_food_id
    self.orig_food_common_name = orig_food_common_name
    self.orig_food_scientific_name = orig_food_scientific_name
    self.orig_food_part = orig_food_part
    self.orig_source_id = orig_source_id
    self.orig_source_name = orig_source_name
    self.orig_content = orig_content
    self.orig_min = orig_min
    self.orig_max = orig_max
    self.orig_unit = orig_unit
    self.orig_citation = orig_citation
    self.citation = citation
    self.citation_type = citation_type
    self.creator_id = creator_id
    self.updater_id = updater_id
    self.created_at = created_at
    self.updated_at = updated_at
    self.orig_method = orig_method
    self.orig_unit_expression = orig_unit_expression
    self.standard_content = standard_content
    self.preparation_type = preparation_type
    self.export = export
    
class MealFoodRelation:
  def __init__(self, id_themeal, id_foodb, public_id_food):
    self.id_themeal = id_themeal
    self.id_foodb = id_foodb
    self.public_id_food = public_id_food 
    

class NutrientIngredient:
  def __init__(self, id_nutrient, id_ingredient):
    self.nutrient_id = id_nutrient
    self.ingredient_id = id_ingredient
    

def ler_csv(nome_arquivo, from_class, isRelathion = False):
  lista_objetos = []
  relathions = {}
  
  with open(nome_arquivo, 'r', encoding="utf8") as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)

      next(leitor_csv, None)

      for linha in leitor_csv:
        # Cria objeto do food que sera armazenado na lista
        if isRelathion:
          relathion = MealFoodRelation(*linha)
          if relathion.id_foodb not in relathions:
            relathions[relathion.id_foodb] = [relathion.id_themeal]
          else:
            relathions[relathion.id_foodb].append(relathion.id_themeal)
          continue
        
        food = from_class(*linha)
      
        lista_objetos.append(food)

  return lista_objetos, relathions

def format_food_nutrient(contents, relathions):
  p_nutrient_food = []
  
  print("Iniciando transformação...")
  
  for content in contents:
    if content.source_type == "Nutrient" and content.food_id in relathions:
      for id in relathions[content.food_id]:
        p_nutrient_food.append(NutrientIngredient(content.source_id, id))
  
  return p_nutrient_food

def escrever_csv_ingredients_nutrients(list, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    print("Iniciando escrita...")
    
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['id_ingredient', 'id_nutrient'])

    for item in list:
        escritor_csv.writerow([item.ingredient_id , item.nutrient_id])
        
  print("Processo Finalizado.")

def main():
  contents, _ = ler_csv('../../../data/raw/Content.csv', FoodData)
  _, relathion_foodb = ler_csv('../../../data/interim/combinacao_food_meal.csv', MealFoodRelation, True)
  
  p_nutrient_food = format_food_nutrient(contents, relathion_foodb)
  
  escrever_csv_ingredients_nutrients(p_nutrient_food, '../../../data/processed/p_ingredients_nutrients.csv')
  
main()