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

    # filename = "the_office-s1_e01-clean.txt"
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

                characters_lines = {}
                characters_words = {}

                for line in script:
                    line = line.rstrip()
                    if re.match(r'^\S+:', line):
                        name = re.findall(r'^\S+:', line)
                        name = name[0][:-1]
                        characters_lines[name] = characters_lines.get(name, 0) + 1
                        line = re.sub(r'\[.*?\]','', line)
                        words = re.findall(r'^\S+:.((\S*\s*)*)', line)
                        words = words[0][0]
                        words = words.translate(line.maketrans('', '', string.punctuation))
                        characters_words[name] = characters_words.get(name, 0) + len(words.split())

                for name, lines in characters_lines.items():
                    words = characters_words[name]
                    line_writer.writerow([season, episode, name, lines, words])






    # with open('employee_file.csv', mode='w') as employee_file:
    # employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    # employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

#     # get total lines and words counts
#     total_lines = sum(characters_lines.values())
#     total_words = sum(characters_words.values())

#     print(characters_lines)

#     loop = True
#     while loop == True:
#         choice = input("Sort by lines or words spoken? (Enter 'lines' or 'words'): ")
#         if choice.lower() == "lines":
#             print()
#             line_count = []
#             for name, lines in list(characters_lines.items()):
#                 line_count.append((lines, name))
#             line_count.sort(reverse=True)
#             for lines, name in line_count:
#                 words = characters_words[name]
#                 pct_words = (words/total_words)*100
#                 pct_lines = (lines/total_lines)*100
#                 dev = (pct_words - pct_lines)
#                 print("%s has %d lines (%s%%) and says %d words (%s%%). (Deviation: %d%%)" % (name, lines, str(pct_lines)[:6], words, str(pct_words)[:6], dev))
#             loop = False
#             break
#         elif choice.lower() == "words":
#             print()
#             word_count = []
#             for name, words in list(characters_words.items()):
#                 word_count.append((words, name))
#             word_count.sort(reverse=True)
#             for words, name in word_count:
#                 lines = characters_lines[name]
#                 pct_words = (words/total_words)*100
#                 pct_lines = (lines/total_lines)*100
#                 dev = (pct_lines - pct_words)
#                 print("%s says %d words (%s%%) and has %d lines(%s%%). (Deviation: %d%%)" % (name, words, str(pct_words)[:6], lines, str(pct_lines)[:6], dev))
#             loop = False
#             break    
#         else:
#             print("Sorry, that\'s not a valid choice.\n")
#             continue
#     print()
