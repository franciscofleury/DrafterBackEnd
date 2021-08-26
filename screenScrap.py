from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq 
import pandas as pd
import numpy as np
from functools import reduce
dataframes = []
nDataframes= []
nDataframesUpdate = []
my_url = ['https://gol.gg/game/stats/31312/page-fullstats/','https://gol.gg/game/stats/31313/page-fullstats/','https://gol.gg/game/stats/31314/page-fullstats/','https://gol.gg/game/stats/31315/page-fullstats/','https://gol.gg/game/stats/31317/page-fullstats/','https://gol.gg/game/stats/31318/page-fullstats/','https://gol.gg/game/stats/31319/page-fullstats/','https://gol.gg/game/stats/31320/page-fullstats/','https://gol.gg/game/stats/31321/page-fullstats/','https://gol.gg/game/stats/31322/page-fullstats/','https://gol.gg/game/stats/31323/page-fullstats/','https://gol.gg/game/stats/31324/page-fullstats/','https://gol.gg/game/stats/31325/page-fullstats/','https://gol.gg/game/stats/31326/page-fullstats/'] 
for url in my_url:
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    df = pd.read_html(str(page_soup.findAll('table')[0]))[0].fillna(0)
    champName = [x['alt'] for x in page_soup.findAll('img',{'class':'rounded-circle'})]
    
    colunas = ['Champion']
    for i in champName:
        if i != 'Kai':
            colunas.append(i)
        else:
            colunas.append("KaiSa")
    df.columns  = colunas
    edited = df.set_index('Champion')
    
    transposed = edited.T.drop('Player',axis=1).drop(['KP%','CS',"CS in Team's Jungle",'CS in Enemy Jungle','CSM','Control Wards Purchased','WPM','VWPM','WCPM','VS%','True Damage','DMG%','K+A Per Minute','GD@15','CSD@15','XPD@15','LVLD@15','Damage dealt to turrets','Time ccing others','Total damage taken','Physical Damage','Magic Damage','GOLD%','Total damage to Champion','Vision Score', 'Wards placed', 'Wards destroyed','KDA'], axis=1)
    
    numeric_columns = ['Kills', 'Deaths', 'Assists', 'Golds',  'GPM'  ,  'VSPM'   ,'DPM', 'Solo kills', 'Double kills', 'Triple kills', 'Quadra kills', 'Penta kills', 'Total heal' ,'Damage self mitigated']
    for column in numeric_columns:
        transposed[column]= pd.to_numeric(transposed[column])
    bonusData = {'Champion':[transposed.index[transposed['Role'] == 'ADC'][0]+'/'+transposed.index[transposed['Role'] == 'SUPPORT'][0],transposed.index[transposed['Role'] == 'ADC'][1]+'/'+transposed.index[transposed['Role'] == 'SUPPORT'][1]],
                 'Role': ['BOT','BOT'],
                 'Kills': [transposed['Kills'].loc[transposed['Role'] == 'ADC'][0]+transposed['Kills'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Kills'].loc[transposed['Role'] == 'ADC'][1]+transposed['Kills'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Deaths': [transposed['Deaths'].loc[transposed['Role'] == 'ADC'][0]+transposed['Deaths'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Deaths'].loc[transposed['Role'] == 'ADC'][1]+transposed['Deaths'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Assists': [transposed['Assists'].loc[transposed['Role'] == 'ADC'][0]+transposed['Assists'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Assists'].loc[transposed['Role'] == 'ADC'][1]+transposed['Assists'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Golds': [transposed['Golds'].loc[transposed['Role'] == 'ADC'][0]+transposed['Golds'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Golds'].loc[transposed['Role'] == 'ADC'][1]+transposed['Golds'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'GPM': [transposed['GPM'].loc[transposed['Role'] == 'ADC'][0]+transposed['GPM'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['GPM'].loc[transposed['Role'] == 'ADC'][1]+transposed['GPM'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'VSPM': [transposed['VSPM'].loc[transposed['Role'] == 'ADC'][0]+transposed['VSPM'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['VSPM'].loc[transposed['Role'] == 'ADC'][1]+transposed['VSPM'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'DPM': [transposed['DPM'].loc[transposed['Role'] == 'ADC'][0]+transposed['DPM'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['DPM'].loc[transposed['Role'] == 'ADC'][1]+transposed['DPM'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Solo kills': [transposed['Solo kills'].loc[transposed['Role'] == 'ADC'][0]+transposed['Solo kills'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Solo kills'].loc[transposed['Role'] == 'ADC'][1]+transposed['Solo kills'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Double kills': [transposed['Double kills'].loc[transposed['Role'] == 'ADC'][0]+transposed['Double kills'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Double kills'].loc[transposed['Role'] == 'ADC'][1]+transposed['Double kills'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Triple kills': [transposed['Triple kills'].loc[transposed['Role'] == 'ADC'][0]+transposed['Triple kills'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Triple kills'].loc[transposed['Role'] == 'ADC'][1]+transposed['Triple kills'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Quadra kills': [transposed['Quadra kills'].loc[transposed['Role'] == 'ADC'][0]+transposed['Quadra kills'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Quadra kills'].loc[transposed['Role'] == 'ADC'][1]+transposed['Quadra kills'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Penta kills': [transposed['Penta kills'].loc[transposed['Role'] == 'ADC'][0]+transposed['Penta kills'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Penta kills'].loc[transposed['Role'] == 'ADC'][1]+transposed['Penta kills'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Total heal': [transposed['Total heal'].loc[transposed['Role'] == 'ADC'][0]+transposed['Total heal'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Total heal'].loc[transposed['Role'] == 'ADC'][1]+transposed['Total heal'].loc[transposed['Role'] == 'SUPPORT'][1]],
                 'Damage self mitigated': [transposed['Damage self mitigated'].loc[transposed['Role'] == 'ADC'][0]+transposed['Damage self mitigated'].loc[transposed['Role'] == 'SUPPORT'][0],transposed['Damage self mitigated'].loc[transposed['Role'] == 'ADC'][1]+transposed['Damage self mitigated'].loc[transposed['Role'] == 'SUPPORT'][1]]}
    bonusDf = pd.DataFrame(bonusData).set_index('Champion')
    bonusDatax = {'Champion':[transposed.index[transposed['Role'] == 'TOP'][0]+'/'+transposed.index[transposed['Role'] == 'JUNGLE'][0],transposed.index[transposed['Role'] == 'TOP'][1]+'/'+transposed.index[transposed['Role'] == 'JUNGLE'][1]],
                 'Role': ['XTOP/JG','XTOP/JG'],
                 'Kills': [transposed['Kills'].loc[transposed['Role'] == 'TOP'][0]+transposed['Kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Kills'].loc[transposed['Role'] == 'TOP'][1]+transposed['Kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Deaths': [transposed['Deaths'].loc[transposed['Role'] == 'TOP'][0]+transposed['Deaths'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Deaths'].loc[transposed['Role'] == 'TOP'][1]+transposed['Deaths'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Assists': [transposed['Assists'].loc[transposed['Role'] == 'TOP'][0]+transposed['Assists'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Assists'].loc[transposed['Role'] == 'TOP'][1]+transposed['Assists'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Golds': [transposed['Golds'].loc[transposed['Role'] == 'TOP'][0]+transposed['Golds'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Golds'].loc[transposed['Role'] == 'TOP'][1]+transposed['Golds'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'GPM': [transposed['GPM'].loc[transposed['Role'] == 'TOP'][0]+transposed['GPM'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['GPM'].loc[transposed['Role'] == 'TOP'][1]+transposed['GPM'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'VSPM': [transposed['VSPM'].loc[transposed['Role'] == 'TOP'][0]+transposed['VSPM'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['VSPM'].loc[transposed['Role'] == 'TOP'][1]+transposed['VSPM'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'DPM': [transposed['DPM'].loc[transposed['Role'] == 'TOP'][0]+transposed['DPM'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['DPM'].loc[transposed['Role'] == 'TOP'][1]+transposed['DPM'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Solo kills': [transposed['Solo kills'].loc[transposed['Role'] == 'TOP'][0]+transposed['Solo kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Solo kills'].loc[transposed['Role'] == 'TOP'][1]+transposed['Solo kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Double kills': [transposed['Double kills'].loc[transposed['Role'] == 'TOP'][0]+transposed['Double kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Double kills'].loc[transposed['Role'] == 'TOP'][1]+transposed['Double kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Triple kills': [transposed['Triple kills'].loc[transposed['Role'] == 'TOP'][0]+transposed['Triple kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Triple kills'].loc[transposed['Role'] == 'TOP'][1]+transposed['Triple kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Quadra kills': [transposed['Quadra kills'].loc[transposed['Role'] == 'TOP'][0]+transposed['Quadra kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Quadra kills'].loc[transposed['Role'] == 'TOP'][1]+transposed['Quadra kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Penta kills': [transposed['Penta kills'].loc[transposed['Role'] == 'TOP'][0]+transposed['Penta kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Penta kills'].loc[transposed['Role'] == 'TOP'][1]+transposed['Penta kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Total heal': [transposed['Total heal'].loc[transposed['Role'] == 'TOP'][0]+transposed['Total heal'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Total heal'].loc[transposed['Role'] == 'TOP'][1]+transposed['Total heal'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Damage self mitigated': [transposed['Damage self mitigated'].loc[transposed['Role'] == 'TOP'][0]+transposed['Damage self mitigated'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Damage self mitigated'].loc[transposed['Role'] == 'TOP'][1]+transposed['Damage self mitigated'].loc[transposed['Role'] == 'JUNGLE'][1]]}
    bonusDfx = pd.DataFrame(bonusDatax).set_index('Champion')
    bonusDatay = {'Champion':[transposed.index[transposed['Role'] == 'MID'][0]+'/'+transposed.index[transposed['Role'] == 'JUNGLE'][0],transposed.index[transposed['Role'] == 'MID'][1]+'/'+transposed.index[transposed['Role'] == 'JUNGLE'][1]],
                 'Role': ['YMID/JG','YMID/JG'],
                 'Kills': [transposed['Kills'].loc[transposed['Role'] == 'MID'][0]+transposed['Kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Kills'].loc[transposed['Role'] == 'MID'][1]+transposed['Kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Deaths': [transposed['Deaths'].loc[transposed['Role'] == 'MID'][0]+transposed['Deaths'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Deaths'].loc[transposed['Role'] == 'MID'][1]+transposed['Deaths'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Assists': [transposed['Assists'].loc[transposed['Role'] == 'MID'][0]+transposed['Assists'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Assists'].loc[transposed['Role'] == 'MID'][1]+transposed['Assists'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Golds': [transposed['Golds'].loc[transposed['Role'] == 'MID'][0]+transposed['Golds'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Golds'].loc[transposed['Role'] == 'MID'][1]+transposed['Golds'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'GPM': [transposed['GPM'].loc[transposed['Role'] == 'MID'][0]+transposed['GPM'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['GPM'].loc[transposed['Role'] == 'MID'][1]+transposed['GPM'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'VSPM': [transposed['VSPM'].loc[transposed['Role'] == 'MID'][0]+transposed['VSPM'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['VSPM'].loc[transposed['Role'] == 'MID'][1]+transposed['VSPM'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'DPM': [transposed['DPM'].loc[transposed['Role'] == 'MID'][0]+transposed['DPM'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['DPM'].loc[transposed['Role'] == 'MID'][1]+transposed['DPM'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Solo kills': [transposed['Solo kills'].loc[transposed['Role'] == 'MID'][0]+transposed['Solo kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Solo kills'].loc[transposed['Role'] == 'MID'][1]+transposed['Solo kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Double kills': [transposed['Double kills'].loc[transposed['Role'] == 'MID'][0]+transposed['Double kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Double kills'].loc[transposed['Role'] == 'MID'][1]+transposed['Double kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Triple kills': [transposed['Triple kills'].loc[transposed['Role'] == 'MID'][0]+transposed['Triple kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Triple kills'].loc[transposed['Role'] == 'MID'][1]+transposed['Triple kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Quadra kills': [transposed['Quadra kills'].loc[transposed['Role'] == 'MID'][0]+transposed['Quadra kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Quadra kills'].loc[transposed['Role'] == 'MID'][1]+transposed['Quadra kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Penta kills': [transposed['Penta kills'].loc[transposed['Role'] == 'MID'][0]+transposed['Penta kills'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Penta kills'].loc[transposed['Role'] == 'MID'][1]+transposed['Penta kills'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Total heal': [transposed['Total heal'].loc[transposed['Role'] == 'MID'][0]+transposed['Total heal'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Total heal'].loc[transposed['Role'] == 'MID'][1]+transposed['Total heal'].loc[transposed['Role'] == 'JUNGLE'][1]],
                 'Damage self mitigated': [transposed['Damage self mitigated'].loc[transposed['Role'] == 'MID'][0]+transposed['Damage self mitigated'].loc[transposed['Role'] == 'JUNGLE'][0],transposed['Damage self mitigated'].loc[transposed['Role'] == 'MID'][1]+transposed['Damage self mitigated'].loc[transposed['Role'] == 'JUNGLE'][1]]}
    bonusDfy = pd.DataFrame(bonusDatay).set_index('Champion')
    transposed =transposed.append(bonusDf)
    transposed =transposed.append(bonusDfx)
    transposed =transposed.append(bonusDfy)
    transposed['id'] = url[26:31]
    dataframes.append(transposed)
    
for i in dataframes:
    
    i['Minutes']= i['Golds'][0]/i['GPM'][0]
    i['Team_Kills']= i['Kills'][0:5].sum()
    i['Team_Kills'][5:]= i['Kills'][5:].sum()
    i['Num_G']= i['Golds']/i['Golds']
    nDataframes.append(i.replace({'Deaths':0,'Team_Kills':0},1))
for n in nDataframes:
    n['KP']= (n['Kills']+n['Assists'])/n['Team_Kills']
    n['KDA_Score']= 1.5*((n['Kills']+n['Assists'])/n['Deaths'])
    n['GPM_Score']=(2.5*n['GPM'])/100
    n['DPM_Score']= n['DPM']/100
    n['KP_Score']= 10*n['KP']
    n['VSPM_Score']= 4*n['VSPM']
    n['TQP_Score']=(3*n['Triple kills'])+(4*n['Quadra kills'])+(5*n['Penta kills'])
    n['HDM_Minutes']= ((n['Total heal']+n['Damage self mitigated'])/n['Minutes'])/150
    n['Final_Score']= (n['KDA_Score']+n['GPM_Score']+n['DPM_Score']+n['KP_Score']+n['VSPM_Score']+n['TQP_Score']+n['HDM_Minutes'])/5
    listaChamps = []
    for index, row in n.iterrows():
        listaChamps.append(index)
    n['Champs'] = listaChamps
    sending = n[['Champs','Role','id','KP_Score','KDA_Score','GPM_Score','DPM_Score','VSPM_Score','TQP_Score','HDM_Minutes','Final_Score']]
    nDataframesUpdate.append(sending)
newData = reduce(lambda  left,right: pd.merge(left,right,on=['Champs','Role'],how='outer'), nDataframes)

groupData= newData.groupby(level=0,axis=1).sum()
onlyData= groupData.fillna(0)
if len(my_url) % 2 == 0:
    onlyData['games']=onlyData['Num_G_x']+onlyData['Num_G_y']
    onlyData['KDA_Score_f']= (onlyData['KDA_Score_x']+onlyData['KDA_Score_y'])/onlyData['games']
    onlyData['GPM_Score_f']= (onlyData['GPM_Score_x']+onlyData['GPM_Score_y'])/onlyData['games']
    onlyData['DPM_Score_f']= (onlyData['DPM_Score_x']+onlyData['DPM_Score_y'])/onlyData['games']
    onlyData['KP_Score_f']= (onlyData['KP_Score_x']+onlyData['KP_Score_y'])/onlyData['games']
    onlyData['VSPM_Score_f']= (onlyData['VSPM_Score_x']+onlyData['VSPM_Score_y'])/onlyData['games']
    onlyData['TQP_Score_f']= (onlyData['TQP_Score_x']+onlyData['TQP_Score_y'])/onlyData['games']
    onlyData['HDM_Score_f']= (onlyData['HDM_Minutes_x']+onlyData['HDM_Minutes_y'])/onlyData['games']
    onlyData['Final_Score_f']= (onlyData['Final_Score_x']+onlyData['Final_Score_y'])/onlyData['games']
else:
    onlyData['games']=onlyData['Num_G_x']+onlyData['Num_G_y']+onlyData['Num_G']
    onlyData['KDA_Score_f']= (onlyData['KDA_Score_x']+onlyData['KDA_Score_y']+onlyData['KDA_Score'])/onlyData['games']
    onlyData['GPM_Score_f']= (onlyData['GPM_Score_x']+onlyData['GPM_Score_y']+onlyData['GPM_Score'])/onlyData['games']
    onlyData['DPM_Score_f']= (onlyData['DPM_Score_x']+onlyData['DPM_Score_y']+onlyData['DPM_Score'])/onlyData['games']
    onlyData['KP_Score_f']= (onlyData['KP_Score_x']+onlyData['KP_Score_y']+onlyData['KP_Score'])/onlyData['games']
    onlyData['VSPM_Score_f']= (onlyData['VSPM_Score_x']+onlyData['VSPM_Score_y']+onlyData['VSPM_Score'])/onlyData['games']
    onlyData['TQP_Score_f']= (onlyData['TQP_Score_x']+onlyData['TQP_Score_y']+onlyData['TQP_Score'])/onlyData['games']
    onlyData['HDM_Score_f']= (onlyData['HDM_Minutes_x']+onlyData['HDM_Minutes_y']+onlyData['HDM_Minutes'])/onlyData['games']
    onlyData['Final_Score_f']= (onlyData['Final_Score_x']+onlyData['Final_Score_y']+onlyData['Final_Score'])/onlyData['games']
scoreData=onlyData[['Role','KDA_Score_f','GPM_Score_f','DPM_Score_f','KP_Score_f','VSPM_Score_f','TQP_Score_f','HDM_Score_f','Final_Score_f','games','Champs']]

Mediana= scoreData['Final_Score_f'].median()
Media= scoreData['Final_Score_f'].mean()
sortData= scoreData.sort_values('Final_Score_f')
roleData= scoreData.sort_values(['Role','Final_Score_f'])
cleanRole= roleData[['Champs','Role','Final_Score_f','games']]
adc= cleanRole.loc[cleanRole['Role']=='ADC']
sup= cleanRole.loc[cleanRole['Role']=='SUPPORT']
mid= cleanRole.loc[cleanRole['Role']=='MID']
jungle= cleanRole.loc[cleanRole['Role']=='JUNGLE']
top= cleanRole.loc[cleanRole['Role']=='TOP']
bestAdc= adc.iloc[[-1]]
bestSup= sup.iloc[[-1]]
bestMid= mid.iloc[[-1]]
bestJungle= jungle.iloc[[-1]]
bestTop= top.iloc[[-1]]
bestComp=pd.concat([bestAdc,bestSup,bestMid,bestJungle,bestTop])
worstAdc= adc.iloc[[0]]
worstSup= sup.iloc[[0]]
worstMid= mid.iloc[[0]]
worstJungle= jungle.iloc[[0]]
worstTop= top.iloc[[0]]
worstComp= pd.concat([worstAdc,worstSup,worstMid,worstJungle,worstTop])
send = {}
for index, row in cleanRole.iterrows():
    send.update({(row['Champs']+'/'+(row['Role'][0].lower())):row['Final_Score_f']})
# print(send)