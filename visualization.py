import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('municipios_rio_de_janeiro.csv')
#print(df.columns)


top_10 = df.head(10)

import numpy as np

x = np.arange(len(top_10["Município"])) 
width = 0.3  

ffig, ax = plt.subplots(figsize=(12, 8))
ax.plot(top_10["Município"], top_10["População Estimada 2024"], marker='o', label='População Estimada 2024')
ax.plot(top_10["Município"], top_10["População Censo 2022"], marker='o', label='População Censo 2022')

ax.set_xlabel('Municípios')
ax.set_ylabel('População')
ax.set_title('População Estimada 2024 vs População Censo 2022')
ax.set_xticklabels(top_10["Município"], rotation=45)
ax.legend()

plt.show()

