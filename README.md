# Manual-Data-Science
Esse é um manual para guiar o andamento de projetos de ciência de dados, a fim de deixar o processo de análise mais organizado aumentando a produtividade para focar mais nos processos de data


# 1- Manual Dos Dados;

<aside>
💡 Verificar os dados que são necessários para começar a construir o projetos e verificar algumas de suas propriedades. Assim já terá um certa noção de alguns processamentos necessário durante o decorrer do projeto

</aside>

Os Metadados são basicamente as propriedades da(s) base de dado(s) que vai ser utilizado para a realização do projeto. 

[Template](https://www.notion.so/Template-000891d83baa45f5913b6afb2f72492d)

- Localização da fonte de dados (Sharepoint, Web…);
- Verificar credenciais para acesso dos dados;

- Atualizações dos dados (em quanto tempo esses dados são atualizados?)
- Verificar a Extensão dos Dados (csv, json, txt…);
- Formato do arquivo;
- Verificar encoding;
- Delimitador;
- 

```python

```

# 2. Data Wrangling

Processo de limpeza e unificação dos conjuntos de dados para facilitar as análises

<aside>
💡 Create a code block by typing `/code` and pressing `enter`.

</aside>

- 
    - 
- Limpeza:
    - Verificar dados duplicados
    - Verificar dados Nan (
    - retirar caracteres especiais
    - Decomposição ou Composição de Colunas
- Formatação:
    - Data/Hora
    - Moeda
    

### 2.1 Checkpoint

Função para salvar resultados intermediários que está sendo realizado dentro do projeto

```python
# Função chekpoint para salvar etapas do andamento do projeto
import numpy as np

def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header = checkpoint_header, data = checkpoint_data)
    checkpoint_variable = np.load(file_name + ".csv") # 
    return(checkpoint_variable)
```

### 2.2 Dados Ausente / Nan

# 3. Modelagem dos Dados

<aside>
💡 Separação do Dataset em dois um com dados numéricos e outro com dados tipo strings

</aside>

### 3.1 Label Encoding - Strings

<aside>
💡 Transformar todos os dados strings em dados numéricos

</aside>

```bash
acme deploy --prod
```

### 3.2 Binarização - String

### 3.3 Limpeza de String

### 3.4 Categorização - String

### 3.5 Formatação de Valores numéricos
