import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://pt.wikipedia.org/wiki/Lista_de_municípios_do_Rio_de_Janeiro_por_população")
soup = BeautifulSoup(page.text, 'html.parser')

#print(soup)
table = soup.find('table', class_='wikitable sortable')
#print(table)
titles = table.find_all('th')
keywords = ['Posição', 'Município', 'População\n(Estimativa 2024)[10]', 'População\n(Censo 2022)', 'Diferença (2024-2022)']

mapping = {
    
    'População\n(Estimativa 2024)[10]': 'População Estimdada 2024',
    'População\n(Censo 2022)': 'População Censo 2022',
    
}
#print(titles)

titles_table = [mapping.get(keyword, keyword) for keyword in keywords if keyword in [title.text.strip() for title in titles]]

#print(titles_table)

pd.DataFrame(columns=titles_table)
df = pd.DataFrame(columns=titles_table)
#print(df)

for row in table.find_all('tr')[2:]:
    columns = row.find_all('td')
    individual_row = [column.text.strip() for column in columns]
  
    while len(individual_row) < len(titles_table):
        individual_row.append('')
    
    length = len(df)
    df.loc[length] = individual_row

df.replace('', pd.NA, inplace=True)
df.dropna(how='all', inplace=True)

#print(df)
df.to_csv('municipios_rio_de_janeiro.csv', index=False)