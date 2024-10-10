from django.middleware.csrf import get_token
from django.http import HttpResponse, HttpRequest

def getToken(req):
    if req.method == "GET":
        print("Check Body in GET")
        token = get_token(req)
        return HttpResponse(token)
    else:
        return HttpResponse("se requiere token")