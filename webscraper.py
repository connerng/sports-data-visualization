from bs4 import BeautifulSoup
import requests
import pandas as pd

url_0304 = 'https://www.basketball-reference.com/players/j/jamesle01/gamelog/2004'

page = requests.get(url_0304)

soup = BeautifulSoup(page.text, features="html.parser")

table = soup.find_all('table')[7]
world_titles = table.find_all('th')

table_titles = [title.text.strip() for title in world_titles][1:30]
df = pd.DataFrame(columns=table_titles)

column_data = table.find_all('tr')
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    if len(individual_row_data) >= 10:
        df.loc[len(df)] = individual_row_data

df['PTS'] = pd.to_numeric(df['PTS'])
df['TRB'] = pd.to_numeric(df['TRB'])
df['AST'] = pd.to_numeric(df['AST'])

pts_sum = 0
reb_sum = 0
ast_sum = 0

pts_seq = []
reb_seq = []
ast_seq = []

for ind in df.index:
    pts_sum += df['PTS'][ind]
    pts_seq.append(pts_sum)
    reb_sum += df['TRB'][ind]
    reb_seq.append(reb_sum)
    ast_sum += df['AST'][ind]
    ast_seq.append(ast_sum)
