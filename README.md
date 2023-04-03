# Breve Guia para Projetos de Análise e Ciência de Dados
Esse é um manual simples e prático para guiar o andamento de projetos de análise e ciência de dados utilizando, a fim de deixar o processo de análise mais organizado aumentando a produtividade para focar mais nos processos no seu código, disponibilizando alguns templates para ser utilizados como base e algumas dicas de código para deixar o seu projeto mais clean e objetivo.

Todos as dicas e templates foram criados do zeros e são os que utilizo em todos os meu projetos de análise de dados

Templates;

- [Trello - Gerencimento de Tarefas](https://trello.com/b/Cb7Rzdex/data-analysis);
- [Figma - Pipeline de Dados](https://www.figma.com/file/a6JA3XC5vdV7VTSBWreZ7H/Template?node-id=0%3A1&t=EfKPDgftA4OTLkSp-1);
[Figma - Mocukp]


## 1 - Origem dos Dados;

<aside>
💡 Verificar os dados que são necessários para começar a construir o projetos e verificar algumas de suas propriedades. Assim já terá uma certa noção de alguns processamentos que vão ser necessários ser realizado no decorrer do projeto.
</aside>

Algumas fontes de dados já possuem Metadados, que traz basicamente todas as propriedades do conjunto de dados em questão. Como o tipo de objeto de cada coluna, tamanho do arquivo, tamanho do dataset… o que já facilita bastante a nossa vida.

Porém nem todas as fontes vão ter de forma tão simples e fácil esses metadados, por isso gosto sempre de criar um resumo com algumas propriedades básicas do conjunto de dados, o que me dá um noção do que vou precisar realizar e assim que consigo ter uma melhor dimensão das análises.

### 1.1 - Metadados
Ao pensar na origem dos dados, é importante entender se o seu projeto utuliza mais de uma origem de fonte de dados, e qual é o processo para acessar essa fonte

- Localização da fonte de dados (Sharepoint, Web, Postgree, Kaggle, MongoDB…);
- Verificar credenciais para acesso dos dados (Organizacional, Chave de acesso...);
- Atualizações dos dados (em quanto tempo esses dados são atualizados?)

### 1.1 - Metadados

- Verificar a Extensão dos Dados (csv, json, txt…);
- Localização da Fonte de Dados;
- Credenciais para acesso dos dados;
- Formato do arquivo;
- Verificar encoding;
- Delimitador;
- Tamaho dos dados;
- Conexão com os dados

### 1.2 - Pipeline de Dados

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cf1cd3bf-8305-4b5e-9b58-4f776624d9a5/Untitled.png)

## Git

## 2. Carregamento dos Dados
<aside>
💡 Carregar os dados da forma correta é imprescindível para evitar possível problemas durante o decorrer do seu projeto, assim como carregar apenas os pacotes que forem necessário ou até mesmo apenas os módulos dos pacotes que forem efetivamente utilizados. Dessa forma é possível deixar o seu projeto mais leve, tanto de memória quanto de processamento.
</aside>

### 2.1 Importação

```python
# importas os pacotes que geralmente são mais utilizados
# lembrando de carregar apenas o que for utilizar
import pandas as pd 
import numpy as np
import matplotlib.pyplot as mlp
import seaborn as sns
```

### 2.2 Configurando as importações

```python
# Configuração dos plots do NumPy
np.set_printoptions(suppress = True, linewidth = 200, precision = 2)
# suppress = 
# linewidth = 
# precision = quantidade de casas decimais
# configuração de impressão do Pandas
pd.
```

```python
# Parâmetros de configuração Matplotlib
from matplotlib import rcParams

rcParams['figure.figsize'] = 12, 4 # tamanho da grade da figura a ser criada
rcParams['lines.linewidth'] = 3 # quantidade de linhas
rcParams['xtick.labelsize'] = 'x-large' # largura do eixo x é o total da tela disponível
rcParams['ytick.labelsize'] = 'x-large' # largura do exio y é o total da tela disponível
```
### 2.3 Checkpoint

Função para salvar resultados intermediários que está sendo realizado dentro do projeto

```python
# Função chekpoint para salvar etapas do andamento do projeto em numpy
import numpy as np

def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header = checkpoint_header, data = checkpoint_data)
    checkpoint_variable = np.load(file_name + ".npz") # testar se funciona com csv
    return(checkpoint_variable)
```

```python
import pandas as pd

def checkpoint(file_name, checkpoint_header, checkpoint_data):
	pd.save(
	return(checkpoint_variable)

```

## Carregando Dataset

<aside>
💡 Carregar o dataset de acordo com a extensão do artigo, e garantir que seja todos os dados sejam devidamente carregados;
</aside>

Pontos a Verificar:

- Encoding;
- Delimitador;
- Escape de Caractere;
- Header (Cabeçalho);
- Concatenar tabelas (recomendo após a limpeza);

## 3 - Data Wrangling/Munging

<aside>
💡 Data Wrangling (ou Data Munging) é o processo de limpeza, transformação e organização dos dados brutos para torná-los mais adequados para análise de dados. Isso pode incluir a remoção de dados ausentes, a correção de dados incorretos ou inconsistentes, a combinação de várias fontes de dados em um único conjunto de dados, entre outras tarefas de preparação de dados..

</aside>

### 3.1 - Formatação de Valores

Formatar corretamente, ou verificar se as colunas do seu dataset estão devidamente configuradas no formato correto para que seja analisadas de formar correta em breve. 

Mesmo que alguns valores já venham formatado como valores numéricos, é importante verificar se por acaso eles não foram carregados em um tipo numérico diferetnte

Uma boa prática é, se possível separa o dataset em questão em dois, um com valores numéricos e outro com valores strings, pois dessa forma poderá ser mais fácil tratar as colunas já que vai ser possível tratar mais de uma coluna de uma única vez.

<aside>
💡 Separar o dataset em dados numéricos e dados do tipo string para facilitar a limpeza dos dados em questão

</aside>

- Formatação dos valores Numéricos;
    - Data/Hora;
    - Moeda (qual região)
    - CEP;
    - Latitude;
    - Tipo numérico (Double, int,);

No caso de caracteres do tipo string, é importante observar se todos os caracteres foram devidamente carregados com o encoding correto, e se há algum escape de caractere.

- Formatação de Caracteres Strings:
    - Endereço por extenso;
    - Cidade;
    - Estado;

# 4 - Análise Exploratória dos Dados - EDA

<aside>
💡 Análise exploratória é uma abordagem inicial de análise de dados que busca entender as principais características e padrões dos dados antes de aplicar técnicas mais avançadas de modelagem ou estatística inferencial. A análise exploratória é geralmente realizada no início de um projeto de análise de dados e pode incluir:

</aside>

z - escore (outliers)

Desvio Padrão

Media

Z-escore

<aside>
💡 O Z-score tem com objetivo identificar os valores que estão acima do desvio padrão dos dados que estão sendo observados

</aside>

```python
from scipy import stats
# Loop por cada variável numérica
for col in nums2:
    
    # Calcula o z-score absoluto
    zscore = abs(stats.zscore(df[col])) 
    
    # Mantém valores com menos de 3 z-score absoluto
    registros = (zscore < 3) & registros
```

### Limpeza dos Dados:

- Verificar dados duplicados
    
    Uma coisa é verificar se existem valores duplicados, outra é se existem linhas duplicadas, para cada tipo de situação é necessário entender o contexto dos dados para 
    
- Verificar dados Nan (Ausentes)
- Verificar caracteres especiais
- Decomposição ou Composição de Colunas

### Tratamento de Valores Ausente / Nan

<aside>
💡 Não é só porque um valor de uma base está ausente, significa que esteja errado. Valor Nulo é diferente de ausente

</aside>

Verificar a quantidade de valores que estão ausente, e de que formas eles estão ausentes, por colunas ou por linha, verificar se na verdade há algum erro no carregamento dos dados ou encoding utilizado

EDA

# 5 - Engenharia de Atributos

<aside>
💡 A Engenharia de atributos é a etapa de criação de novas variáveis ou atributos (também chamados de features) a partir dos dados brutos para melhorar o desempenho dos modelos de Machine Learning. Essa etapa envolve a seleção e transformação de variáveis existentes, bem como a criação de novas variáveis que podem ser mais relevantes para o modelo. Isso pode incluir a criação de variáveis de tempo, variáveis categóricas, variáveis numéricas ou combinações de várias variáveis.

</aside>

```bash
acme deploy --prod
```

# Pré-Processamento de Dados;

<aside>
💡 O Pré-Processamento de dados é utilizando sempre que for necessário utilizar machine learning, transformando simplificando todas as variáveis. Modificando os dados, sem perder a informação

</aside>

### Label Encoding - Strings

Label Encoding (codificação de rótulos) é uma técnica de codificação para lidar com variáveis categóricas. Nesta técnica, a cada rótulo é atribuído um número inteiro exclusivo com base na ordem alfabética. Na codificação de rótulos em Python, substituímos o valor categórico por um valor numérico entre 0 e o número de classes menos 1. Se o valor da variável categórica contiver 5 classes distintas usamos (0, 1, 2, 3 e 4). Observe que os dados são modificados, mas sem perder a informação que eles representam. Isso pode ser feito de maneira manual (usando dicionários em Python) ou com o algoritmo Label Encoder do pacote Scikit-Learn.

### One Hot Encoding

Nessa abordagem, para cada categoria de um recurso, criamos uma nova coluna (às vezes chamada de variável fictícia) com codificação binária (0 ou 1) para indicar se uma determinada linha pertence a essa categoria.Vamos considerar aimagem abaixo. Observe que a variável Color possui 3 categorias (Red, Yellow e Green). 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8a3174d-e4b8-4398-9869-76f018dcb145/Untitled.png)

Aplicando One-Hot Encoding3 novas variáveis são criadas, sendo o valor 1 quando a ocorrência daquela cor e 0 quando não há ocorrência.Uma potencial desvantagem desse método é um aumento significativo na dimensionalidade do conjunto de dados (que é chamado de Curse of Dimensionality).Ou seja, a codificação one-hot é o fato de estarmos criando colunas adicionais, uma para cada valor exclusivo no conjunto do atributo categórico que gostaríamos de codificar. 

Portanto, se tivermos um atributo categórico que contenha, digamos, 1.000 valores exclusivos, essa codificação one-hot gerará 1.000 novos atributos adicionais e isso não é desejável. Para simplificar, a codificação one-hot é uma ferramenta bastante poderosa, mas só é aplicável para dados categóricos que possuem um número baixo de valores exclusivos. One-Hot Encoding é o processo de criação de variáveis fictícias.

