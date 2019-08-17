import numpy as np
import pandas as pd
import matplotlib.pyplot

df = pd.read_csv('the_office-all_episodes-database.csv')

characters = np.sort(df['character'].unique())

for character in characters:
    print(character)

michael_spellings = [
Micael
Micahel
Michae
Michael
Michael 
Michael &amp; Dwight
Michael &amp; Holly
Michael and Andy
Michael and Christian
Michael and Darryl
Michael and Donna
Michael and Dwight
Michael and Erin
Michael and Holly
Michael and Jim
Michael and Samuel together
Michael's Ad
Michael/Dwight
Michal
Micheal
Michel
Mihael
Miichael
]