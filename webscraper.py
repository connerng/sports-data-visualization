from bs4 import BeautifulSoup
import requests
import pandas as pd

url_sea = 'https://www.pro-football-reference.com/teams/sea/2023/gamelog/'

page = requests.get(url_sea)

soup = BeautifulSoup(page.text, features="html.parser")

table = soup.find_all('table')[0]
world_titles = table.find_all('th')

table_titles = [title.text.strip() for title in world_titles][8:44]
table_titles[8] = 'PTS'
table_titles[9] = 'PA'
weeks = [title.text.strip() for title in world_titles][44:]
df = pd.DataFrame(columns=table_titles)

column_data = table.find_all('tr')
i = 0
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    if len(individual_row_data) > 0:
        individual_row_data.insert(0, weeks[i])
        i += 1
        df.loc[len(df)] = individual_row_data
    # print(individual_row_data)

# print(df)

df['PTS'] = pd.to_numeric(df['PTS'])
df['PA'] = pd.to_numeric(df['PA'])

pts_sum = 0
pts_seq = []

for ind in df.index:
    pts_sum += df['PTS'][ind]
    pts_seq.append(pts_sum)

print(pts_seq)