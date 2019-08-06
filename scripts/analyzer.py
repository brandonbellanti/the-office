import numpy as np
import pandas
import matplotlib.pyplot as plt

csv_file = 'the_office-all_episodes-database.csv'
df = pandas.read_csv(csv_file)

gb = df.groupby(['season','character'])
print(gb['words'].sum())

# # plot character
# character = df[(df.character == 'Jim')]
# seasons = character.groupby('season')
# means = seasons.words.mean()
# means.plot.bar(x='episode', y='lines')
# plt.show()


# # plot entire season
# season_four = df[df.season == 4]
# characters = season_four.groupby(['character'])
# means = characters.words.mean()
# means.plot(kind='pie', x='character',y='words')
# plt.show()


# # plot specific episode
# fun_run = df[(df.season == 4) & (df.episode == 1)]
# fun_run.set_index('character', inplace=True)
# fun_run.plot.pie(y='lines')
# plt.show()