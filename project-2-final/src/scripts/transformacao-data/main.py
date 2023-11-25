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


def ler_csv(nome_arquivo, from_class):
  lista_objetos = []

  with open(nome_arquivo, 'r', encoding="utf8") as arquivo_csv:
      leitor_csv = csv.reader(arquivo_csv)

      next(leitor_csv, None)

      for linha in leitor_csv:
          # Cria objeto do food que sera armazenado na lista
          food = from_class(*linha)

          lista_objetos.append(food)

  return lista_objetos

def escrever_csv(lista_ingredientes, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['ID', 'Nome', 'Descrição', 'Tipo'])

    for ingrediente in lista_ingredientes:
        escritor_csv.writerow([ingrediente.id_ingredient, ingrediente.str_ingredient, ingrediente.str_description, ingrediente.str_type])

def compara_ingredient_plant(ingredient, food):
    # Verifica se o name da planta está contido no str_ingredient do ingrediente
    
    words = ingredient.str_ingredient.lower().split()
    
    for word in words:
      if word in food.name.lower() or word[:-1] in food.name.lower():
        return True
        
    return False
    
    # return distancia_palavras(ingredient.str_ingredient.lower(), food.name.lower()) <= 2
    # return ingredient.str_ingredient.lower() in food.name.lower()

def encontrar_combinacoes(lista_ingredientes, lista_foods):
    combinacoes = []

    # for ingrediente in lista_ingredientes:
    #     achou = False
    #     for food in lista_foods:
    #         # Se a condição for satisfeita, adiciona os IDs à lista de combinações
    #         if compara_ingredient_plant(ingrediente, food):
    #             combinacoes.append({'id_ingredient': ingrediente.id_ingredient,
    #                                 'id_plant': food.id})
    #             food.founded = True
    #             achou = True
    #             break
                
    #     if not achou:
    #       print(ingrediente.id_ingredient, ingrediente.str_ingredient)
    
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
      
      if food_minin == None: continue
      print(ingrediente.id_ingredient, ingrediente.str_ingredient.lower(), '-', food_minin.id, food_minin.name)
      combinacoes.append({'id_ingredient': ingrediente.id_ingredient, 'id_food': food_minin.id})
                

    return combinacoes

def main():
  food_list = ler_csv("../../../data/raw/Food.csv", Food)
  ingredient_list = ler_csv("../../../data/external/ingredientes.csv", Ingredient)
  
  print(len(encontrar_combinacoes(ingredient_list, food_list)))
  
main()