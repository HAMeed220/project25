from django.shortcuts import render

# Create your views here

from app.models import *
from django.http import HttpResponse 


def form_html(request):
    if request.method=='POST':
        ta=request.POST['ta']

        TO=Topic.objects.get_or_create(topic_name=ta)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topic':QLTO}
        return render (request,'display_topic.html',d)
    return render(request,'form_html.html')

def form_wh(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        ta=request.POST['ta']
        na=request.POST['na']
        ur=request.POST['ur']
        el=request.POST['el']

        TO=Topic.objects.get(topic_name=ta)

        WO=Webpages.objects.get_or_create(topic_name=TO,name=na,url=ur,email=el)[0]
        WO.save()
        QLWO=Webpages.objects.all()
        d1={'Webpages':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'form_wh.html',d)

def form_accessrec(request):
    QLWO=Webpages.objects.all()
    d1={'Webpages':QLWO}

    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']

        WO=Webpages.objects.get(name=na)

        AO=AccessRecord.objects.get_or_create(name=WO,date=da,author=au)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        d2={'AccessRecord1':QLAO}
        return render(request,'display_accessR.html',d2)

    return render(request,'form_accessrec.html',d1)

def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('ta')

        QLWO=Webpages.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpages.objects.filter(topic_name=i)
        d1={'Webpages':QLWO}

        return render(request,'display_webpage.html',d1) 
       
    return render(request,'select_multiple_webpage.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
 
    return render(request,'checkbox.html',d) 

def select_multiple_accessrecord(request):
    QLWO=Webpages.objects.all()
    d1={'Webpages':QLWO}
     
    if request.method=='POST':
        namelist=request.POST.getlist('na')

        QLAO=AccessRecord.objects.none()
        for na in namelist:
            QLAO=QLAO|AccessRecord.objects.filter(name=na)

        d2={'AccessRecord1':QLAO}
        return render(request,'display_accessR.html',d2)
    return render(request,'select_multiple_accessrecord.html',d1)

def check_box(request):
    QLWO=Webpages.objects.all()
    d1={'Webpages':QLWO}

    return render(request,'check_box.html',d1) 
