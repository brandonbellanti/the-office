import numpy as np
import pandas as pd
import matplotlib.pyplot

df = pd.read_csv('the_office-all_episodes-database.csv')

characters = np.sort(df['character'].unique())

# for character in characters:
#     print(character)

bad_spellings = {
    'AJ':['AJ, A.J.'],
    'All': [
        'All',
        'All Girls',
        'All but Oscar',
        'All the Men',
        'Everybody',
        'Everyone',
        'Everyone watching',
        'Group',
        'Group chant'
    ],
    'Andy': [
        'Andy',
        'Andy &amp; Erin',
        'Andy &amp; Michael',
        'Andy &amp; Walter',
        'Andy and Darryl',
        'Andy and Dwight',
        'Andy and Erin',
        'Andy and Jim',
        'Andy and Michael',
        'Andy/Oscar',
        'Andy/Stanley',
        'Video Andy',
        'sAndy'
    ],
    'Angela': [
        'Angel',
        'Angela',
        'Angela &amp; Oscar',
        'Angela and Dwight',
        'Angela/Pam',
        'Angels',
        'Anglea',
    ],
    'Bob': ['Bob','Bob Vance'],
    'Carol': ['Carol', 'Carol Stills', 'Carrol', 'Carroll'],
    'Charles': ['Chares','Charles'],
    'David':['Dacvid Walalce','Dacvid Wallace','David','David Wallace','David Wallcve'],
    'Darryl':[
        'Darrly',
        'Darry',
        'Darryl',
        'Darryl &amp; Oscar',
        'Darryl and Andy',
        'Darryl and Angela',
        'Darryl and Katy',
        'Darryl and Kevin',
        "Darryl's sister",
        'Daryl',
    ],
    'Deangelo':[
        'DeAgnelo',
        'DeAngelo',
        'Deangelo',
        'Deangelo/Michael',
        'Denagelo',
    ],
    'Delivery person': [
        'Delivery',
        'Delivery Boy',
        'Delivery Guy',
        'Delivery Woman',
        'Delivery man',
        'Deliveryman',
    ],
    'Dwight': [
        'Dwight',
        'Dwight ' ,
        'Dwight &amp; Andy',
        'Dwight &amp; Nate',
        'Dwight and Andy',
        'Dwight and Angela',
        'Dwight and Erin',
        'Dwight and Michael',
        'Dwight and Roy',
        'Dwight.',
        'DwightKSchrute',
    ],
    'Gabe': ['Gabe','Gabe/Kelly/Toby', 'abe'],
    'Hank': ['Hank','Hank ', 'Hank the Security Guard'],
    'Helene': ["(Pam's mom) Heleen",'Helen','Helene'],
    'Holly': ['Holly','Holy ', 'Holly &amp; Darryl', 'Holly &amp; Michael'],
    'Isabel': ['Isabel', 'Isabelle'],
    'Jim': [
        'JIM9334',
        'JIM9334 ',
        'JIm',
        'Jim',
        'Jim ',
        'Jim &amp; Dwight',
        'Jim &amp; Pam',
        'Jim and Dwight',
        'Jim and Pam',
        'Mr. Halpert',
        ' Jim'
    ],
    'Jo': [' Jo','Jo','Jo Bennett'],
    'Kelly': ['Kelly','Kelly and Erin'],
    'Kevin': [
        'Kevin',
        'Kevin &amp; Andy',
        'Kevin &amp; Meredith',
        'Kevin &amp; Oscar'
    ],
    'Mee-Maw': ['MeeMaw','Mee-Maw'],
    'Meredith': ['Meredith','Meridith'],
    'Michael': [
        'Micael',
        'Micahel',
        'Michae',
        'Michael',
        'Michael ',
        'Michael &amp; Dwight',
        'Michael &amp; Holly',
        'Michael and Andy',
        'Michael and Christian',
        'Michael and Darryl',
        'Michael and Donna',
        'Michael and Dwight',
        'Michael and Erin',
        'Michael and Holly',
        'Michael and Jim',
        'Michael and Samuel together',
        "Michael's Ad"
        'Michael/Dwight',
        'Michal',
        'Micheal',
        'Michel',
        'Mihael',
        'Miichael',
        'M ichael',
        'MIchael',
        'Video Michael'
    ],
    'Nellie': ['Nellie', 'Nellie Bertram', 'Nellie and Pam'],
    'Oscar': [
        "Oscar",
        "Oscar and Stanley",
        "Oscar's Computer",
        "Oscar's friend",
        "Oscar's voice from the computer",
    ],
    'Pam': [
        'Pam',
        'Pam ',
        'Pam &amp; Dwight',
        'Pam and Jim',
        'Pam and Kelly',
        'Pam and others',
        'Pam as fourth-biggest client',
        'Pam as ninth-biggest client',
        'Pam/Jim'
    ],
    'Phillip':['Phillip','Philip','Senator','Senator Lipton','Senator Liptop'],
    'Phyllis': [
        'Phylis',
        'Phyliss',
        'Phyllis',
        'Phyllis and Creed'
    ],
    'Receptionist': [
        'Receptionist',
        'Receptionitis15',
        'Receptionitis15 '
    ],
    'Robert': [
        'Robert',
        'Robert &amp; Creed',
        'Robert California'
    ],
    'Ryan': [
        'Ryan',
        'Ryan Howard',
        'Ryan and Kelly',
        'Ryan and Michael',
        'Ryan and others',
        "Ryan's Voicemail"
    ],
    'Stanley': [
        'Stanely',
        'Stanley',
        'Stanley &amp; Phyllis'
    ],
    'Todd': ['Todd','Todd Packer'],
    'Walter': ['Walter','Walter &amp; Walter Jr'],
    'Walter Jr.': ['Walter Jr','Walt Jr.'],
}

for name, bad_spelling in bad_spellings.items():
    df['character'][df['character'].isin(bad_spelling)] = name

print(df.head(1000))