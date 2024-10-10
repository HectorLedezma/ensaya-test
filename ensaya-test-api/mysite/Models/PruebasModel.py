from django.http import HttpResponse, HttpRequest
from mysite.Connection import connection

def getOneTest(id):
    connect = connection.connectMongoDB()
    try:
        collection = connect.get_collection("Pruebas")
        data = collection.find({"id":id})
        return data
    except Exception as e:
        return {"Error":e}


def UploadNewTest(data):
    connect = connection.connectMongoDB()
    collection = connect.get_collection("Pruebas")
    try:
        collection.insert_one(data)
        return {"OK":"OK"}
    except Exception as e:
        return {"Error":e}
    