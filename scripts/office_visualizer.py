import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import click
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.tokenize import word_tokenize
import string



@click.command()
@click.option('-s','--season', help='Enter the season number.', type=int)
@click.option('-e','--episode', help='Enter the episode number.', type=int)
@click.option('-c','--character', help='Enter the character name.', type=str)
@click.option('-b','--sortby', help="Sort results by 'words' or 'lines.'", default='lines', type=click.Choice(['words', 'lines']))
# @click.option('-b','--groupby', help="Group results by 'show', 'season', 'episode.'", default='season', type=click.Choice(['episode', 'season','show']))


def plot_data(season, episode, character, sortby):
    """"Show visualizations for words and lines from the American version of 'The Office'"""
    df = pd.read_csv('the_office-all_episodes.csv')


    # df.set_index(['season', 'episode','character'], inplace=True)
    if season:
        df = df[df['season'] == season]
    if episode:
        df = df[df['episode'] == episode]
    if character:
        df = df[df['character'] == character]
    
    
    # # count words
    # df['line'] = df['line'][df['line'].notnull()].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    # df['line'] = df['line'][df['line'].notnull()].apply(lambda x: x.lower())
    # df['line'] = df['line'][df['line'].notnull()].apply(lambda x: [word for word in word_tokenize(x) if not word in stop])
   
    # df['line'].apply(pd.Series).stack().value_counts().nlargest(20).plot(kind="barh")
    # plt.title('Most commonly used words')
    # plt.gca().invert_yaxis()
    # plt.show()

    # quit()


    df = df[df['character_type'].isin(['main','recurring'])]

    if not character:
        grouped = (df.groupby(['character'])['line'].count().sort_values(ascending=True))

    if character:
        grouped = df.groupby(['season'])['line'].count() / len(df.groupby(['episode']))

    print(grouped)
    ax = grouped.plot.barh()
    ax.set_yticklabels(grouped.keys())
    plt.xlabel('Characters')
    plt.ylabel('Line count')
    plt.title("The Office")
    plt.show()

plot_data()