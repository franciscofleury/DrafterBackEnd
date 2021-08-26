import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate('D:\\Documents\\ServerFirebase\\lolfantasyadmin.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def clearScore(name):
    scoreDoc = db.collection('ChampScores').document('Scores').get()
    if scoreDoc.exists:
        
        db.collection('ChampScores').document('Scores').collection('historico').document(name).set(scoreDoc.to_dict())
        db.collection('ChampScores').document('Scores').set({})

def voltar(name):
    returnDoc = db.collection('ChampScores').document('Scores').collection('historico').document(name).get()
    db.collection('ChampScores').document('Scores').set(returnDoc.to_dict())

def pageClear(name):
    pagesDoc = db.collection('ChampScores').document('pages').collections()
    for col in pagesDoc:
        if col.id != 'hist':
            for doc in col.stream():
                db.collection('ChampScores').document('pages').collection('hist').document(name).collection(col.id).document(doc.id).set(doc.to_dict())
                db.collection('ChampScores').document('pages').collection(col.id).document(doc.id).delete()

while True:
    inp = input('Digite um comando: ')
    if inp == 'clear score':
        rodada = input('Qual rodada? ')
        clearScore(rodada)
    elif inp == 'stop' or inp == 'exit' or inp == 'sair':
        break
    elif inp == 'hist pages score':
        pageRodada = input('Qual rodada? ')
        pageClear(pageRodada)
    elif inp =='volta':
        rodadaVolt = input('Qual rodada?')
        voltar(rodadaVolt)
    

