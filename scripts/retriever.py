import requests
import time

seasons = {1:6, 2:22, 3:23, 4:14, 5:26, 6:24, 7:24, 8:24, 9:23}

for season, episodes in list(seasons.items()):
        for episode in range(1, episodes + 1):
                episode = str(episode)
                if len(episode) < 2:
                        episode = "0"+episode
                # print('the_office-s%s_e%s.txt' % (season, episode))
                url = 'http://officequotes.net/no%s-%s.php' % (season, episode)
                data = requests.get(url)
                with open('the_office-s%s_e%s-raw.txt' % (season, episode),'w') as out_f:
                        out_f.write(str(data.text.encode('utf-8')))
                # time.sleep(1)
