[Link Binder](https://mybinder.org/v2/gh/MrRay0708/Projeto-MC536/main)

## Motivação e Contexto

Sabemos que cada região do mundo tem a sua cultura, sua história, suas visões, seus costumes, suas realidades e sua própria culinária. A ideia aqui é não só entender o perfil nutricional de cada receita, ou mesmo somente entender a composição quimica das mesmas, em uma análise mais profunda, com as bases de dados que vamos usar, conseguimos traçar um perfil nutricional ou um perfil de consumo com base nas receitas de cada região, tentando entender os alimentos mais usados para cada uma. 

## Slides

### Apresentação Prévia
> Coloque aqui o link para o PDF da apresentação prévia

### Apresentação Final
> Coloque aqui o link para o PDF da apresentação final

## Modelo Conceitual Revisado

![Modelo](https://github.com/MrRay0708/Projeto-MC536/blob/main/project-2-final/assets/mer.png)

## Modelo Lógico Revisado

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

## Dataset Publicado
> Se ao tratar e integrar os dados originais foram produzidas novas bases relacionais ou de grafos, elencar essas bases.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

## Bases de Dados

Título da base | Link | Breve descrição
----- | ----- | -----
FoodDB | [link](https://www.foodb.ca/) | Uma base com diversos alimentos e suas composições tanto quimicas como com relação aos nutrientes encotrados em cada alimento
TheMealDB | [link](https://www.themealdb.com/) | Uma base com diversas receitas e seus ingredientes, relacionando elas com seus países/regiões de origem

## Detalhamento do Projeto

### Extração dos dados e construção do dataset

A extração de dados foi algo trabalhoso dentro do nosso trabalho. Escolhemos duas bases, o FoodDB  e o TheMealDB, a principal dificuldade era conseguir relacionar os alimentos da tabela Food do FoodDB com os ingredientes da tabela de ingredientes da base do TheMealDB. Eles não usam o mesmo tipo de chave, o que leva a nós termos que fazer ligações pelo nome dos alimentos, o que pode dificultar bastante o processo. 

Antes de comentar dessa parte, é importante ressaltar que o TheMealDB não possue os dados em uma planilha, somente os disponibiliza na API dele. Portanto, uma etapa anterior foi fazermos scripts ([link](https://github.com/MrRay0708/Projeto-MC536/tree/main/project-2-final/src/scripts/transform_api_json_para_csvs_themeal)) para conseguir não só extrair todos os dados pela API da base de dados, mas também ao mesmo tempo criar os .csv, sem perca de dados.

Com esses dados extraídos do TheMealDB e todos em .csv, o próximo processo seria facilitado (mas ainda assim complicado). A nossa próxima etapa seria conseguir, para todos os ingredientes do TheMealDB, uma relação com algum food no FoodDB. Nenhum ingrediente do TheMealDB poderia ficar de fora, já que são a base para a análise de receitas. A pergunta que nos começamos a fazer foi: "Como conseguir fazer essa relação entre duas tabelas, de forma automática (já que são muitos dados), e ao mesmo tempo de forma eficiente?". No fim das contas, não bastava somente nós conseguirmos as relações, mas depois ter que revisar de uma em uma para ter certerza que não tem nenhuma relação absurda.

Nossa estratégia para resolver isso foi simplismente começar do básico: o pensamento mais lógico é, vamos ver quem tem nomes iguais em ambas as tabelas e relacionar. O resultado, obviamente, não foi dos melhores, mais da metade dos ingredientes ficaram sem relacionamentos. É claro, é de se esperar que alguns nomes sejam escritos de maneira diferente. A segunda estratégia seria tentar trabalhar com substring, o que gerou um resultado melhor, mas, ainda assim, mais de 25% dos ingredientes ainda estavam sem relacionamentos. Nesse momento, tivemos que pensar em uma abordagem diferente.

Quando formos analisar mais a fundo as bases, vimos que teriamos outro problema: singular e plural. Tem alguns alimentos que, dentro do FoodDB, estavam no singular, e no TheMealDB estavam no plural (ou vice e versa). Foi então que tivemos que recorrer a um algoritmo que alguns de nós vimos na matéria de "Desafios de Programação": um algoritmo de progração dinâmica, para saber a distância de duas strings, ou seja, você consegue passar duas strings para ele e ele te retorna, em quantos caracteres essas duas strings se diferenciam. Esse seria uma ótima saída para nós, mas não bastava somente usar ele.

Então fizemos um algoritmo ([link](https://github.com/MrRay0708/Projeto-MC536/tree/main/project-2-final/src/scripts/transformacao-dados)) que, além de usar esse algoritmo de programação dinâmica, se utiliza de outros critérios como substrings e até mesmo igualdade de strings, para identificar e fazer as relações entre os ingredientes do TheMealDB e os alimentos do FoodDB. Se fossemos resumir o algoritmo, basicamente para cada ingrediente (TheMeal), ele roda um loop para cada alimento (Food), e separa dentro disso, cada palavra dentro do nome de ambos (ingrediente e alimento) e faz a comparação usando o algoritmo de programação dinâmica. Para cada combinação de ingrediente e alimento, temos um número que indica o quanto aquele ingrediente "se parece" com aquele alimento (com alguns critérios de desempate). O alimento que se parecer mais com aquele ingrediente, segundo esses critérios, será o alimento do FoodDB que "se relacionará" com o ingrediente do TheMealDB.

Com esse algoritmo, conseguimos achar uma relação para quase todos os ingredientes do TheMealDB. Sobrando só alguns que tivemos que realmente interpletar e achar uma relação manualmente, não sendo muito trabalhoso. 

### Análises feitas

## Evolução do Projeto

Na primeira versão do projeto, tinhamos já uma ideia de trabalhar com bases de relacionadas a receitas, entretanto tivemos alguns problemas no momento de escolher as bases: na nossa primeira versão, tinhamos bases demais e não conseguimos dimencionar o trabalho que seria para modelar e juntar tantas bases diferentes. Algumas bases inclusive, não seriam tão uteis para as análises que gostariamos de fazer. Depois de algumas conversas, resolvemos diminuir o numero de bases (deixando apenas duas) e fazer uma remodelagem no nosso modelo conceitual, deixando ele um pouco mais simples, mas o suficiente para as análises que gostariamos de fazer. 

Uma das bases que retiramos foi uma base que tinha pesquisas sobre o consumo de nutrientes de diversas pessoas. Ainda que fossem dados interessantes, só tinhamos informação de nutrientes, então teriamos que relacionar a tabela com nutrientes e só assim relacionar com os alimentos (ingredientes), o que deixaria o processo de extração e modelagem de dados muito mais trabalhoso do que já foi. Nesse caso, deixamos essa parte de lado simplificar o projeto e focar nas análises que queriamos, que é sobre as receitas em diversas regiões.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

### Perguntas/Análise com Resposta Implementada

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
