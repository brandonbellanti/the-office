import re
import string
import csv
import json

with open('the_office-all_episodes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\nThe categories are: {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}.\n')
            line_count += 1
        else:
            print(f'Season {row[1]}, episode {row[2]}.')
            print(f'\tThe line counts are: {row[3]}')
            print(f'\tThe word counts are: {row[4]}\n')
            line_count += 1