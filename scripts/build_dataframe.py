import re
import string
import csv
import json

seasons = {1:6, 2:22, 3:23, 4:14, 5:26, 6:24, 7:24, 8:24, 9:23}

show = "The Office"
season = 1
episode = 1

with open('the_office-all_episodes-database.csv', 'w') as all_episodes:

    line_writer = csv.writer(all_episodes, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    line_writer.writerow(['season', 'episode', 'character', 'lines', 'words'])

    for season, episodes in list(seasons.items()):
        for episode in range(1, episodes + 1):
            episode = str(episode)
            if len(episode) < 2:
                    episode = "0"+episode
            filename = "the_office-s%s_e%s-clean.txt" % (season, episode)
            # all_episodes.write('%s\n'%filename)
            # print('%s\n'%filename)

            # read file and count lines and words per character
            with open(filename, 'r') as script:

                for line in script:
                    line = line.rstrip()
                    line = line.split(':',1)
                    if len(line)>1:
                        name = line[0]
                        line = line[1]
                    else:
                        pass
                    # print(name, line)
                    line_writer.writerow([season, episode, name, line])
                    # print(line)
                    # if re.match(r'^\S+:', line):
                    #     name = re.findall(r'^\S+:', line)
                    #     name = name[0][:-1]
                    #     characters_lines[name] = characters_lines.get(name, 0) + 1
                    #     # line = re.sub(r'\[.*?\]','', line)
                    #     # words = re.findall(r'^\S+:.((\S*\s*)*)', line)
                    #     line = ':'.split()
                    #     words = words[0][0]
                    #     print(line)

                        # words = words.translate(line.maketrans('', '', string.punctuation))
                        # characters_words[name] = characters_words.get(name, 0) + len(words.split())

                # for name, lines in characters_lines.items():
                #     words = characters_words[name]
