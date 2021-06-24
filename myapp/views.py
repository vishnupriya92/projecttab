from django.shortcuts import render

# Create your views here.


from myapp.models import Topic,Webpage,AccessDetails

def dbdat(request):
    topics=Topic.objects.all()
    webpages=Webpage.objects.all()
    return render(request,"dbdata.html",context={"topics":topics,"webpages":webpages})


