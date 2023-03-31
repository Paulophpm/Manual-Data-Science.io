# Breve Manual para Data Science
Esse é um manual simples e prático para guiar o andamento de projetos de ciência de dados utilizando o Phyton, a fim de deixar o processo de análise mais organizado aumentando a produtividade para focar mais nos processos de data, disponibilizando alguns templates para ser utilizados como base e algumas dicas de código para deixar o seu projeto mais clean e objetivo.

Esse projeto tem como objetivo que você entenda a teoria por trás do código das etapas necessárias a serem realizadas em um projeto de data science, a depender do projeto as etpas e dos dados utilizados, pode ser que seja necessário pular algumas etapas, ou até menos durante o seu projeto seja necessário voltar a uma etapa anterior para resilver algum problema.

# 1 - Pre-Carregamento dos Dados;

<aside>
💡 Verificar os dados que são necessários para começar a construir o projetos e verificar algumas de suas propriedades. Assim já terá uma certa noção de alguns processamentos que vão ser necessários ser realizado no decorrer do projeto.
</aside>

Algumas fontes de dados já possuem Metadados, que traz basicamente todas as propriedades do conjunto de dados em questão. Como o tipo de objeto de cada coluna, tamanho do arquivo, tamanho do dataset… o que já facilita bastante a nossa vida.

Porém nem todas as fontes vão ter de forma tão simples e fácil esses metadados, por isso gosto sempre de criar um resumo com algumas propriedades básicas do conjunto de dados, o que me dá um noção do que vou precisar realizar e assim que consigo ter uma melhor dimensão das análises.

[Template](https://www.notion.so/Template-000891d83baa45f5913b6afb2f72492d)

### 1.1 - Origem
Ao pensar na origem dos dados, é importante entender se o seu projeto utuliza mais de uma origem de fonte de dados, e qual é o processo para acessar essa fonte

[Template Origem](https://www.figma.com/file/a6JA3XC5vdV7VTSBWreZ7H/Template?node-id=0%3A1&t=EfKPDgftA4OTLkSp-1)

- Localização da fonte de dados (Sharepoint, Web, Postgree, Kaggle, MongoDB…);
- Verificar credenciais para acesso dos dados (Organizacional, Chave de acesso...);
- Atualizações dos dados (em quanto tempo esses dados são atualizados?)

### 1.2 - Metadados

- Verificar a Extensão dos Dados (csv, json, txt…);
- Formato do arquivo;
- Verificar encoding;
- Delimitador;
- Tamaho dos dados;
- Conexão com os dados

# 2. Carregamento dos Dados
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

# Parâmetros de configuração Seasborn
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

# 3 - Data Wrangling

<aside>
💡 Data Wrangling (ou Data Munging) é o processo de limpeza, transformação e organização dos dados brutos para torná-los mais adequados para análise de dados. Isso pode incluir a remoção de dados ausentes, a correção de dados incorretos ou inconsistentes, a combinação de várias fontes de dados em um único conjunto de dados, entre outras tarefas de preparação de dados..

</aside>

### 1.1 - Formatação de Valores

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

