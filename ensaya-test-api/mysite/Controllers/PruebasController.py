from mysite.Models import PruebasModel
from django.http import HttpResponse, HttpRequest

def creaEnsayo(req):
    body = req.body
    RawData = PruebasModel.getOneTest(body.id)#Datos en Burto
    Data = RawData
    HttpResponse(Data)#Datos procesados


def SubeEnsayo(req):
    body = req.body
    res = PruebasModel.UploadNewTest(body)
    HttpResponse(res)


