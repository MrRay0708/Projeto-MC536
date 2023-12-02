import csv

class ChemicalCompound:
    def __init__(self, id, public_id, name, moldb_iupac, state, annotation_quality, description, cas_number, moldb_inchikey, moldb_inchi, moldb_smiles, moldb_mono_mass, kingdom, superklass, klass, subklass):
        self.id = id
        self.public_id = public_id
        self.name = name
        self.moldb_iupac = moldb_iupac
        self.state = state
        self.annotation_quality = annotation_quality
        self.description = description
        self.cas_number = cas_number
        self.moldb_inchikey = moldb_inchikey
        self.moldb_inchi = moldb_inchi
        self.moldb_smiles = moldb_smiles
        self.moldb_mono_mass = moldb_mono_mass
        self.kingdom = kingdom
        self.superklass = superklass
        self.klass = klass
        self.subklass = subklass

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

    escritor_csv.writerow(['compound_id', 'public_id', 'name'])

    for item in list:
        escritor_csv.writerow([item.id , item.public_id, item.name])
        
  print("Processo Finalizado.")


def main():
  compounds = ler_csv('../../../data/raw/Compound.csv', ChemicalCompound)
  
  escrever_csv_compounds(compounds, '../../../data/processed/p_compounds.csv')
  
main()