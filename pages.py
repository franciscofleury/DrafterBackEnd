import pandas as pd
from screenScrap import nDataframesUpdate

from collections import defaultdict

champ_data = defaultdict(list)

for i, n in enumerate(nDataframesUpdate):
    for index, value in n.iterrows():
        role = value['Role'].lower()[0]
        name = str(value['Role'].lower()[0])+index.lower().replace('/','-')
        
    
        champ_data[name].append(n.loc[(n['Champs'] == index) & (role == name[0])])
print(champ_data)