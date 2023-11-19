
## Modelo lógico revisado

```
Categoria(_id_, nome)

Regiao(_id_, nome)

Grupo(_id_, nome)

Receita(_id_, titulo, fonte, instrucoes, regiao_id, categoria_id)
  regiao_id chave estrangeira -> Regiao(id)
  categoria_id chave estrangeira -> Categoria(id)

Ingrediente(_id_, nome, grupo_id)
  grupo_id chave estrangeira -> Grupo(id)

ReceitaIngrediente(_receita_id_, _ingrediente_id_, qtde)
  _receita_id_ chave estrangeira -> Receita(id)
  _ingrediente_id_ chave estrangeira -> Ingrediente(id)

Nutriente(_id_, nome)

IngredienteNutriente(_ingrediente_id_, _nutriente_id_, valor, min, max)
  _ingrediente_id_ chave estrangeira -> Ingrediente(id)
  _nutriente_id_ chave estrangeira -> Nutriente(id)

ComponenteQuimico(_id_, nome, formula)

IngredienteComponenteQuimico(_ingrediente_id_, _componenteQuimico_id_)
  _ingrediente_id_ chave estrangeira -> Ingrediente(id)
  _componenteQuimico_id_ chave estrangeira -> ComponenteQuimico(id)
```
