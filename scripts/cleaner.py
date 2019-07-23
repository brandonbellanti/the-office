import re
from bs4 import BeautifulSoup


seasons = {1:6, 2:22, 3:23, 4:14, 5:26, 6:24, 7:24, 8:24, 9:23}

for season, episodes in list(seasons.items()):
        for episode in range(1, episodes + 1):
                episode = str(episode)
                if len(episode) < 2:
                        episode = "0"+episode

                with open("the_office-s%s_e%s-raw.txt" % (season, episode), 'r') as file:
                    soup = BeautifulSoup(file, 'html.parser')
                    soup = soup.find_all('div','quote')
                    soup = str(soup)


                    with open("the_office-s%s_e%s-clean.txt" % (season, episode), 'w') as out_file:
                        # out_file.write(str(soup))
                        lines = soup.split('<br/>')
                        for line in lines:
                            line = re.sub(r'^.*<b>', '', line)
                            line = re.sub('</b>','', line)
                            line = line.replace('\\', '')
                            out_file.write(line + '\n')
