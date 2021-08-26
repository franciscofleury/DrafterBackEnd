import firebase_admin
from firebase_admin import credentials, firestore
from screenScrap import send
from pages import champ_data
import pandas as pd
from google.cloud.firestore_v1 import Increment

cred = credentials.Certificate('D:\\Documents\\ServerFirebase\\lolfantasyadmin.json')
default_app = firebase_admin.initialize_app(cred)


db = firestore.client()
db.collection('ChampScores').document('Scores').set(send)
for key, value in champ_data.items():
    
    
    for i in value:
        
        to_send ={'Champs':i['Champs'][0],'Role':i['Role'][0],'id':i['id'][0],'Final_Score':i['Final_Score'][0],'KDA_Score':i['KDA_Score'][0],'GPM_Score':i['GPM_Score'][0],'DPM_Score':i['DPM_Score'][0],'KP_Score':i['KP_Score'][0],'VSPM_Score':i['VSPM_Score'][0],'TQP_Score':float(i['TQP_Score'][0]),'HDM_Score':float(i['HDM_Minutes'][0])}
        
        print(to_send)
        
        db.collection('ChampScores').document('pages').collection(key).document(i['id'][0]).set(to_send)