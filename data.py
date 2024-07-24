from bs4 import BeautifulSoup
import requests
import pandas as pd


url_sea = 'https://www.pro-football-reference.com/teams/sea/2023/gamelog/'
url_sf = 'https://www.pro-football-reference.com/teams/sfo/2023/gamelog/'
url_la = 'https://www.pro-football-reference.com/teams/ram/2023/gamelog/'
url_az = 'https://www.pro-football-reference.com/teams/crd/2023/gamelog/'

urls = [url_az, url_la, url_sea, url_sf]
teams = ['Cardinals', 'Rams', 'Seahawks', '49ers']
sequences = []

for url in urls:

    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    table = soup.find_all('table')[0]
    world_titles = table.find_all('th')
    table_titles = [title.text.strip() for title in world_titles][8:17]
    table_titles[8] = 'PTS'
    weeks = [title.text.strip() for title in world_titles][44:]

    # create dataframe
    df = pd.DataFrame(columns=table_titles)
    zeroRow = ['0', '', '', '', '', '', '', '', '0']
    df.loc[len(df)] = zeroRow

    # add web data to dataframe
    column_data = table.find_all('tr')
    i = 0
    for row in column_data:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data][:8]
        if len(individual_row_data) > 0:
            individual_row_data.insert(0, weeks[i])
            i += 1
            df.loc[len(df)] = individual_row_data

    # edit df
    df = df.drop(['Day', 'Date', '', 'OT', 'Opp'], axis=1)
    df['Week'] = pd.to_numeric(df['Week'])
    df['PTS'] = pd.to_numeric(df['PTS'])


    # find bye week
    for i in range(len(df)):
        if df.loc[i]['Week'] != i:
            bye_week = i
            break

    # add bye week row
    newRow = [bye_week, 0]
    for i in range(len(df), bye_week, -1):
        df.loc[i] = df.loc[i-1]
        
    df.loc[bye_week] = newRow


    # create points sequence
    pts_sum = 0
    pts_seq = []

    for ind in df.index:
        pts_sum += df['PTS'][ind]
        pts_seq.append(pts_sum)
    
    sequences.append(pts_seq)
    print(pts_seq)
