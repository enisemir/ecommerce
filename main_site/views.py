from django.shortcuts import render_to_response, HttpResponse
from panel.models import Indexslider

def index(request):
    tumu = Indexslider.objects.all()
    c = {"request": request,
         "tumu": tumu}
    return render_to_response("index.html", c)
