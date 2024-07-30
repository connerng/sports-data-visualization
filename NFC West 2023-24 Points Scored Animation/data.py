from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

# url_az = 'https://www.pro-football-reference.com/teams/crd/2023/gamelog/'
# url_atl = 'https://www.pro-football-reference.com/teams/atl/2023/gamelog/'
# url_bal = 'https://www.pro-football-reference.com/teams/rav/2023/gamelog/'
# url_buf = 'https://www.pro-football-reference.com/teams/buf/2023/gamelog/'
# url_car = 'https://www.pro-football-reference.com/teams/car/2023/gamelog/'
# url_chi = 'https://www.pro-football-reference.com/teams/chi/2023/gamelog/'
# url_cin = 'https://www.pro-football-reference.com/teams/cin/2023/gamelog/'
# url_cle = 'https://www.pro-football-reference.com/teams/cle/2023/gamelog/'
# url_dal = 'https://www.pro-football-reference.com/teams/dal/2023/gamelog/'
# url_den = 'https://www.pro-football-reference.com/teams/den/2023/gamelog/'
# url_det = 'https://www.pro-football-reference.com/teams/det/2023/gamelog/'
# url_gb = 'https://www.pro-football-reference.com/teams/gnb/2023/gamelog/'
# url_hou = 'https://www.pro-football-reference.com/teams/htx/2023/gamelog/'
# url_ind = 'https://www.pro-football-reference.com/teams/clt/2023/gamelog/'
# url_jax = 'https://www.pro-football-reference.com/teams/jax/2023/gamelog/'
# url_kc = 'https://www.pro-football-reference.com/teams/kan/2023/gamelog/'
# url_lv = 'https://www.pro-football-reference.com/teams/rai/2023/gamelog/'
# url_lac = 'https://www.pro-football-reference.com/teams/sdg/2023/gamelog/'
url_lar = 'https://www.pro-football-reference.com/teams/ram/2023/gamelog/'
url_mia = 'https://www.pro-football-reference.com/teams/mia/2023/gamelog/'
url_min = 'https://www.pro-football-reference.com/teams/min/2023/gamelog/'
# url_ne = 'https://www.pro-football-reference.com/teams/nwe/2023/gamelog/'
# url_no = 'https://www.pro-football-reference.com/teams/nor/2023/gamelog/'
# url_nyg = 'https://www.pro-football-reference.com/teams/nyg/2023/gamelog/'
# url_nyj = 'https://www.pro-football-reference.com/teams/nyj/2023/gamelog/'
# url_phi = 'https://www.pro-football-reference.com/teams/phi/2023/gamelog/'
# url_pit = 'https://www.pro-football-reference.com/teams/pit/2023/gamelog/'
# url_sf = 'https://www.pro-football-reference.com/teams/sfo/2023/gamelog/'
# url_sea = 'https://www.pro-football-reference.com/teams/sea/2023/gamelog/'
# url_tb = 'https://www.pro-football-reference.com/teams/tam/2023/gamelog/'
# url_ten = 'https://www.pro-football-reference.com/teams/oti/2023/gamelog/'
# url_wsh = 'https://www.pro-football-reference.com/teams/was/2023/gamelog/'


# urls = [url_az, url_atl, url_bal, url_buf, url_car, url_chi, url_cin, url_cle, url_dal, url_den, url_det, url_gb, 
#         url_hou, url_ind, url_jax, url_kc, url_lv, url_lac] 
urls = [url_lar, url_mia, url_min
        # url_ne, url_no, url_nyg, url_nyj, url_phi, url_pit, url_sf, 
        # url_sea, url_tb, url_ten, url_wsh
        ]
teams = [
    # "Arizona Cardinals",
    # "Atlanta Falcons",
    # "Baltimore Ravens",
    # "Buffalo Bills",
    # "Carolina Panthers",
    # "Chicago Bears",
    # "Cincinnati Bengals",
    # "Cleveland Browns",
    # "Dallas Cowboys",
    # "Denver Broncos",
    # "Detroit Lions",
    # "Green Bay Packers",
    # "Houston Texans", 
    # "Indianapolis Colts",
    # "Jacksonville Jaguars",
    # "Kansas City Chiefs",
    # "Las Vegas Raiders",
    # "Los Angeles Chargers",
    "Los Angeles Rams",
    "Miami Dolphins",
    "Minnesota Vikings",
#     "New England Patriots",
#     "New Orleans Saints",
#     "New York Giants",
#     "New York Jets",
#     "Philadelphia Eagles",
#     "Pittsburgh Steelers",
#     "San Francisco 49ers",
#     "Seattle Seahawks",
#     "Tampa Bay Buccaneers",
#     "Tennessee Titans",
#     "Washington Commanders"
]
sequences = []

teamIndex=0
for url in urls:

    page = requests.get(url)
    print(page)
    if page.status_code == 200:
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
        networkError = False
    else:
        print("Network Error")
        networkError = True

# CSV
header =['Team', 'Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10',
         'Week 11', 'Week 12', 'Week 13', 'Week 14', 'Week 15', 'Week 16', 'Week 17', 'Week 18']

if not networkError:
    with open('NFC West 2023-24 Points Scored Animation/pointsbyweek.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(0, len(teams)):
            curTeam = [teams[i]]
            writer.writerow(curTeam + sequences[i])



    