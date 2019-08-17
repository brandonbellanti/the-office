import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import click

main_characters = ['Michael','Jim','Dwight','Pam','Phyllis','Stanley','Oscar','Angela','Creed','Darryl','Kevin','Ryan','Kelly','Toby','Meredith','Andy','Erin','Stanley']
recurring_characters = ['Jan','David','Katy','Bob','Hank','Karen','Robert','Deangelo','AJ','Jo','Pete','Charles', 'Holly','Gabe', 'Nate','Mose','Clark','Nellie']


@click.command()
@click.option('-s','--season', help='Enter the season number.', type=int)
@click.option('-e','--episode', help='Enter the episode number.', type=int)
@click.option('-c','--character', help='Enter the character name.', type=str)
@click.option('-b','--sortby', help="Sort results by 'words' or 'lines.'", default='lines', type=click.Choice(['words', 'lines']))
@click.option('-b','--groupby', help="Group results by 'show', 'season', 'episode.'", default='season', type=click.Choice(['episode', 'season','show']))


def plot_data(season, episode, character, sortby, groupby):
    """"Show visualizations for words and lines from the American version of 'The Office'"""
    df = pd.read_csv('the_office-all_episodes-database.csv')

    # df.set_index(['season', 'episode','character'], inplace=True)
    if season:
        df = df[df['season'] == season]
    if episode:
        df = df[df['episode'] == episode]
    if character:
        df = df[df['character'] == character]
    
    grouped = df.groupby(['character'])[sortby].sum().sort_values(ascending=False)
    print(grouped)
    grouped = grouped.head(20)
    ax = grouped.plot.bar()
    ax.set_xticklabels(grouped.keys())
    plt.xlabel('Characters')
    plt.ylabel(sortby.capitalize())
    plt.title("The Office")
    plt.show()

plot_data()