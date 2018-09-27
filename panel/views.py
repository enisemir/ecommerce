from django.shortcuts import render_to_response, HttpResponse
from django.core.context_processors import csrf
from panel.models import Indexslider


def index(request):
    if request.POST:
        anasayfa_slider = Indexslider()

        anasayfa_slider.slogan = request.POST["slogan"]
        anasayfa_slider.icerik = request.POST["icerik"]

        anasayfa_slider.save()

        c = {"request": request}
        c.update(csrf(request))

        return render_to_response("panel_index.html", c)
    c = {"request": request}
    c.update(csrf(request))
    return render_to_response("panel_index.html", c)

def indexedit(request):

    duzenlenecekveri = Indexslider.objects.get(id=1)
    c = {"request": request,
         "duzenlenecekveri": duzenlenecekveri}
    c.update(csrf(request))

    if request.POST:
        duzenlenecekveri.slogan = request.POST["slogan"]
        duzenlenecekveri.icerik = request.POST["icerik"]

        duzenlenecekveri.save()

    return render_to_response("panel_indexedit.html", c)
    c = {"request": request}
    c.update(csrf(request))
    return render_to_response("panel_indexedit.html", c)

def indexdelete(request):

    silinecekveri = Indexslider.objects.get(id=1)
    silinecekveri.delete()
    c = {"request": request}
    c.update(csrf(request))
    return render_to_response("panel_indexedit.html")





