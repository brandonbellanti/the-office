import matplotlib.pylab as plt
import csv
import ast
import numpy as np
import click
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')


season = input("\nEnter season number: ")
episode = input("Enter episode number: ")
print()

if len(episode) < 2:
    episode = "0"+episode

with open('the_office-all_episodes-dictionaries.csv','r') as csv_file:
    read_file = csv.DictReader(csv_file, fieldnames=['show', 'season', 'episode', 'characters_lines', 'characters_words'])
    for row in read_file:
        if row['season'] == season and row['episode'] == episode:
            line_count = row['characters_lines']
            word_count = row['characters_words']

    loop = True
    while loop == True:
        choice = input("Sort by lines or words spoken? (Enter 'lines' or 'words'): ")
        if choice.lower() == "lines":
            data = line_count
            loop = False
            break
        elif choice.lower() == "words":
            data = word_count
            loop = False
            break    
        else:
            print("Sorry, that\'s not a valid choice.\n")
            continue
    print()

data = ast.literal_eval(data)

plt.bar(data.keys(), data.values())
plt.xlabel('Character')
plt.ylabel('%s spoken' % choice.capitalize())
plt.xticks(rotation=90)
for x,y in data.items():
    plt.text(x,y,str(y))
plt.title('The Office | Season %s, Episode %s' % (season, episode))
plt.show()
