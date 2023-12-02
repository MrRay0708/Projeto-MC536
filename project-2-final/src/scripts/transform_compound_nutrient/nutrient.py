import csv

class Nutrient:
    def __init__(self, id, legacy_id, type, public_id, name, export, state, annotation_quality, description, wikipedia_id, comments, dfc_id, duke_id, eafus_id, dfc_name, compound_source, metabolism, synthesis_citations, general_citations, creator_id, updater_id, created_at, updated_at):
        self.id = id
        self.legacy_id = legacy_id
        self.type = type
        self.public_id = public_id
        self.name = name
        self.export = export
        self.state = state
        self.annotation_quality = annotation_quality
        self.description = description
        self.wikipedia_id = wikipedia_id
        self.comments = comments
        self.dfc_id = dfc_id
        self.duke_id = duke_id
        self.eafus_id = eafus_id
        self.dfc_name = dfc_name
        self.compound_source = compound_source
        self.metabolism = metabolism
        self.synthesis_citations = synthesis_citations
        self.general_citations = general_citations
        self.creator_id = creator_id
        self.updater_id = updater_id
        self.created_at = created_at
        self.updated_at = updated_at

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

def escrever_csv_compounds(list, nome_arquivo):
  with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    print("Iniciando escrita...")
    
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(['nutrient_id', 'public_id', 'legacy_id', 'name'])

    for item in list:
        escritor_csv.writerow([item.id , item.public_id, item.legacy_id, item.name])
        
  print("Processo Finalizado.")


def main():
  compounds = ler_csv('../../../data/raw/Nutrient.csv', Nutrient)
  
  escrever_csv_compounds(compounds, '../../../data/processed/p_nutrients.csv')
  
main()