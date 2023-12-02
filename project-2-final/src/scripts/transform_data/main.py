import csv

class Food:
    def __init__(self, id, name, name_scientific, description, itis_id, wikipedia_id,
        picture_file_name, picture_content_type, picture_file_size,
        picture_updated_at, legacy_id, food_group, food_subgroup,
        food_type, created_at, updated_at, creator_id, updater_id,
        export_to_afcdb, category, ncbi_taxonomy_id, export_to_foodb,
        public_id):
      self.id = id
      self.name = name
      self.name_scientific = name_scientific
      self.description = description
      self.itis_id = itis_id
      self.wikipedia_id = wikipedia_id
      self.picture_file_name = picture_file_name
      self.picture_content_type = picture_content_type
      self.picture_file_size = picture_file_size
      self.picture_updated_at = picture_updated_at
      self.legacy_id = legacy_id
      self.food_group = food_group
      self.food_subgroup = food_subgroup
      self.food_type = food_type
      self.created_at = created_at
      self.updated_at = updated_at
      self.creator_id = creator_id
      self.updater_id = updater_id
      self.export_to_afcdb = export_to_afcdb
      self.category = category
      self.ncbi_taxonomy_id = ncbi_taxonomy_id
      self.export_to_foodb = export_to_foodb
      self.public_id = public_id
      self.founded = False
      
class Ingredient:
    def __init__(self, id_ingredient, str_ingredient, str_description, str_type):
      self.id_ingredient = id_ingredient
      self.str_ingredient = str_ingredient
      self.str_description = str_description
      self.str_type = str_type


class ProcessedIngredient:
  def __init__(self, food: Food, ingredient: Ingredient, food_group: dict()) -> None:
    self.id = ingredient.id_ingredient
    self.name = ingredient.str_ingredient
    self.description = ingredient.str_description
    self.id_group = food_group[food.food_group]


def distancia_palavras(a, b):
  n = len(a)
  m = len(b)

  t = [[] for _ in range(n + 1)]
  for i in range(n + 1):
    t[i] = [0 for _ in range(m + 1)]

  for i in range(n + 1):
    t[i][0] = i
  for j in range(m + 1):
    t[0][j] = j

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      add = 1
      if (a[i - 1] == b[j - 1]): add = 0
      t[i][j] = t[i - 1][j - 1] + add
      t[i][j] = min(t[i][j], t[i - 1][j] + 1)
      t[i][j] = min(t[i][j], t[i][j - 1] + 1)

  return t[n][m]


def ler_csv(nome_arquivo, from_class, isFood = False):
  lista_objetos = []
  lista_grupos = {}

  k = 0
  with open(nome_arquivo, 'r', encoding="utf8") as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)

      next(leitor_csv, None)

      for linha in leitor_csv:
          # Cria objeto do food que sera armazenado na lista
          food = from_class(*linha)

          lista_objetos.append(food)

          if (isFood and food.food_group not in lista_grupos):
            k += 1
            lista_grupos[food.food_group] = k

  return lista_objetos, lista_grupos

def escrever_csv_comb(list, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['id_themeal', 'id_foodb', 'public_id_food'])

    for item in list:
        escritor_csv.writerow([item['id_ingredient'], item['id_food'], item['public_id_food']])

def escrever_csv_processed(list, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['id', 'name', 'description', 'group_id'])

    for item in list:
        escritor_csv.writerow([item.id, item.name, item.description, item.id_group])

def escrever_csv_group(dict, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['id', 'description_group'])

    for item in dict.keys():
        escritor_csv.writerow([dict[item], item])

def compara_ingredient_plant(ingredient, food):
    # Verifica se o name da planta está contido no str_ingredient do ingrediente
    
    words = ingredient.str_ingredient.lower().split()
    
    for word in words:
      if word in food.name.lower() or word[:-1] in food.name.lower():
        return True
        
    return False
    
    # return distancia_palavras(ingredient.str_ingredient.lower(), food.name.lower()) <= 2
    # return ingredient.str_ingredient.lower() in food.name.lower()

def encontrar_combinacoes(lista_ingredientes, lista_foods, groups):
    combinacoes = []
    processedIngredients = []
    
    print('Calculando combinações...')

    for ingrediente in lista_ingredientes:
      achou = False

      minin = 0
      food_minin = None

      for food in lista_foods:

        palavras_ingredientes = ingrediente.str_ingredient.lower().split()
        palavras_food = food.name.lower().split()

        cont = 0
        for palavra_ingrediente in palavras_ingredientes:
          for palavra_food in palavras_food:

            if(distancia_palavras(palavra_ingrediente, palavra_food) <= 1):
              cont += 1

        if(minin < cont):
          minin = cont
          food_minin = food
        elif(minin == cont and food_minin != None):
          cont1 = 0
          for palavra_ingrediente in palavras_ingredientes:
            for palavra_food in food_minin.name.split():
              if palavra_ingrediente == palavra_food:
                cont1 += 1

          cont2 = 0
          for palavra_ingrediente in palavras_ingredientes:
            for palavra_food in palavras_food:
              if palavra_ingrediente == palavra_food:
                cont2 += 1

          if(cont2 > cont1):
            minin = cont
            food_minin = food
      
      if food_minin == None: 
        combinacoes.append({'id_ingredient': ingrediente.id_ingredient, 'id_food': '', 'public_id_food': ''})
        continue
      
      combinacoes.append({'id_ingredient': ingrediente.id_ingredient, 'id_food': food_minin.id, 'public_id_food': food_minin.public_id})
      processedIngredients.append(ProcessedIngredient(food_minin, ingrediente, groups))

    print('Calculo finalizado')

    return combinacoes, processedIngredients

def main():
  food_list, groups = ler_csv("../../../data/raw/Food.csv", Food, True)
  ingredient_list, _ = ler_csv("../../../data/external/ingredientes.csv", Ingredient)
  
  comb, processed = encontrar_combinacoes(ingredient_list, food_list, groups)

  escrever_csv_comb(comb, '../../../data/interim/combinacao_food_meal.csv')
  escrever_csv_processed(processed, '../../../data/processed/p_ingredients.csv')
  escrever_csv_group(groups, '../../../data/processed/p_groups.csv')

  
main()