# -*- coding: utf-8 -*-
"""Profissao_Analista_de_dados_M2_Exercicio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cpnfTzYw_-5_Y18R6suJrJTrXUdvP_Ey

<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo** | Python: Estruturas de Dados
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Listas;</li>
  <li>Conjuntos;</li>
  <li>Dicionários.</li>
</ol>

---

# **Exercícios**

## 1\. Listas

Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.
"""

filmes = ['Um sonho de liberdade', 'O poderoso chefao', 'Batman', 'O poderoso chefao II', '12 homens e uma sentenca', 'A lista de Schindler', 'O senhor dos aneis', 'Pulp Fiction', 'O senhor dos aneis: sociedade do anel', 'Tres homens em conflito']

print(filmes)

"""Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.


"""

primeiro_filme = filmes.pop(0)
segundo_filme = filmes.pop(0)

print(filmes)

filmes.insert(0, segundo_filme)
filmes.insert(1, primeiro_filme)

print(filmes)

"""---

## 2\. Conjuntos

Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
"""

filmes = ['O poderoso chefao', 'Um sonho de liberdade', 'Batman', 'O poderoso chefao II', '12 homens e uma sentenca', 'A lista de Schindler', 'O senhor dos aneis', 'Pulp Fiction', 'O senhor dos aneis: sociedade do anel', 'Tres homens em conflito']

ultimos_filmes = ['Pulp Fiction', 'O senhor dos aneis: sociedade do anel', 'Tres homens em conflito']

filmes_duplicados = filmes + ultimos_filmes

print(filmes_duplicados)

"""Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado."""

filmes_duplicados = list(set(filmes + ultimos_filmes))

print(filmes_duplicados)
print(len(filmes_duplicados))

"""---

## 3\. Dicionários

Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>, 'sinopse': <sinopse do filme>}`.
"""

dicionario_filmes = []

filmes = {'nome': 'Um sonho de liberdade', 'ano': '1994', 'sinopse': 'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'O poderoso chefao', 'ano': '1972', 'sinopse': 'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'Batman', 'ano': '2008', 'sinopse': 'Quando a ameaça conhecida como O Coringa surge de seu passado, causa estragos e caos nas pessoas de Gotham. O Cavaleiro das Trevas deve aceitar um dos maiores testes para combater a injustiça.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'O poderoso chefao II', 'ano': '1974', 'sinopse': 'Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque.'}
dicionario_filmes.append(filmes)

filmes = {'nome': '12 homens e uma sentenca', 'ano': '1957', 'sinopse': 'O julgamento de um assassinato em Nova Iorque é frustrado por um único membro, cujo ceticismo forca o júri a considerar cuidadosamente evidências antes de dar o veredito.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'A lista de Schindler', 'ano': '1993', 'sinopse': 'Na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler começa a ser preocupar com seus trabalhadores judeus depois de testemunhar sua perseguição pelos nazistas.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'O senhor dos aneis', 'ano': '2003', 'sinopse': 'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'Pulp Fiction', 'ano': '1994', 'sinopse': 'As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'O senhor dos aneis: sociedade do anel', 'ano': '2001', 'sinopse': 'Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas.'}
dicionario_filmes.append(filmes)

filmes = {'nome': 'Tres homens em conflito', 'ano': '1966', 'sinopse': 'Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério.'}
dicionario_filmes.append(filmes)

print(dicionario_filmes)