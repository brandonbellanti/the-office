import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import click


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
    
    df = df[df['character_type'].isin(['main','recurring'])]
    grouped = (df.groupby(['character'])['line'].count().sort_values(ascending=True))
    print(grouped)
    ax = grouped.plot.barh()
    ax.set_yticklabels(grouped.keys())
    plt.xlabel('Characters')
    plt.ylabel('Line count')
    plt.title("The Office")
    plt.show()

plot_data()