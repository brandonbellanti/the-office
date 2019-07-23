import re
import string
import matplotlib.pylab as plt

# ask user for season and episode
print()
season = input("Enter season number: ")
episode = input("Enter episode number: ")
if len(episode) < 2:
    episode = "0"+episode

try:
    filename = "the_office-s%s_e%s-clean.txt" % (season, episode)
    # filename = "s1e1.txt"
    characters_lines = {}
    characters_words = {}
    title = None

    # read file and count lines and words per character
    with open(filename, 'r') as script:
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

    # get total lines and words counts
    total_lines = sum(characters_lines.values())
    total_words = sum(characters_words.values())

    print(characters_lines)

    loop = True
    while loop == True:
        choice = input("Sort by lines or words spoken? (Enter 'lines' or 'words'): ")
        if choice.lower() == "lines":
            print()
            line_count = []
            for name, lines in list(characters_lines.items()):
                line_count.append((lines, name))
            line_count.sort(reverse=True)
            for lines, name in line_count:
                words = characters_words[name]
                pct_words = (words/total_words)*100
                pct_lines = (lines/total_lines)*100
                dev = (pct_words - pct_lines)
                print("%s has %d lines (%s%%) and says %d words (%s%%). (Deviation: %d%%)" % (name, lines, str(pct_lines)[:6], words, str(pct_words)[:6], dev))
            loop = False
            break
        elif choice.lower() == "words":
            print()
            word_count = []
            for name, words in list(characters_words.items()):
                word_count.append((words, name))
            word_count.sort(reverse=True)
            for words, name in word_count:
                lines = characters_lines[name]
                pct_words = (words/total_words)*100
                pct_lines = (lines/total_lines)*100
                dev = (pct_lines - pct_words)
                print("%s says %d words (%s%%) and has %d lines(%s%%). (Deviation: %d%%)" % (name, words, str(pct_words)[:6], lines, str(pct_lines)[:6], dev))
            loop = False
            break    
        else:
            print("Sorry, that\'s not a valid choice.\n")
            continue
    print()

except:
    print("\nSorry, that script could not be found.")