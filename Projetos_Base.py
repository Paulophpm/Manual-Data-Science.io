import pandas as pd
import numpy as np
import matplotlib.pyplot as mlp
import seaborn as sns

# Função chekpoint para salvar etapas do andamento do projeto em numpy

def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header = checkpoint_header, data = checkpoint_data)
    checkpoint_variable = np.load(file_name + ".csv") # 
    return(checkpoint_variable)
  
# Configuração de impressão do NumPy
np.set_printoptions(suppress = True, linewidth = 200, precision = 2)
# configuração de impressão do Pandas
pd.s

# Parâmetros de configuração Matplotlib
from matplotlib.plyplot import rcParams



# Parâmetros de configuração Seasborn
