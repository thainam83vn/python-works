from pymongo import  MongoClient

client = MongoClient()

def importAmex():
    db = client.finance
    db.symbol
