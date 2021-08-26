import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

cred = credentials.Certificate('D:\\Documents\\ServerFirebase\\lolfantasyadmin.json')
default_app = firebase_admin.initialize_app(cred)


db = firestore.client()

def excel(name):
    doc = db.collection('ChampScores').document('Scores').get().to_dict()
    dfDoc = pd.DataFrame.from_dict(doc, orient='index')
    print(dfDoc)
    dfDoc.to_excel(r'D:\\Documents\\PontosRodadas\\'+name+'.xlsx')

while True:
    inp = input('QUAL RODADA: ')
    if inp in ['exit','quit','sair']:
        break
    else:
        excel(inp)