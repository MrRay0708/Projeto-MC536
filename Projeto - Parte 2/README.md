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

![Modelo](https://github.com/MrRay0708/Projeto-MC536/blob/main/Projeto%20-%20Parte%202/Projeto%20-%20NovoER.png)

## Perguntas/análises revisadas


### Pergunta/Análise 1
Quais os nutrientes mais consumidos em cada país?
- A ideia aqui é fazer uma relação entre as receitas de cada país e os nutrientes que mais aparecem nessas receitas, entendendo um pouco do perfil nutricional de cada pais

### Pergunta/Análise 2
Quais os ingredientes que compõe determinadas receitas?
- Mapear o relacionamento entre receitas e ingredientes

### Pergunta/Análise 3
Quais os ingredientes mais consumidos? E em cada regiões?
- A partir das receitas identificar os ingredientes mais típicos de cada país e de maneira geral

### Pergunta/Análise 4
Dado um conjunto de nutrientes e uma faixa de valor, quais são as regiões que tem um consumo adequado desse nutriente dentro dessa faixa de valor?
- Aqui podemos tentar entender o valor nutricional das receitas de cada região, dado um nutriente, ver quais regiões consomem de forma adequada esse nutriente, a partir da receita e de seus ingredientes.

### Pergunta/Análise 5
Dado as receitas de determinada categoria, quais são os componentes que menos aparecem? E quais são os que mais aparecem? 
- Aqui conseguimos ver componentes quimicos que são importantes para o ser humano (ou que podem ser prejudiciais) e verificar o quanto eles aparecem nas receitas de uma categoria específica. Podendo até mesmo tentar relacionar com a região da receita.
	
### Pergunta/Análise 6
Dado um grupo específico de ingredientes, quais são os nutrientes mais/menos abundantes e quais são os componentes mais/menos abundantes? Conseguimos relacionar isso com a região de receitas que tem esses ingredientes?
- Por essa análise, conseguimos ver o impacto de determinado componente para o perfil nutricional desse grupo em específico
