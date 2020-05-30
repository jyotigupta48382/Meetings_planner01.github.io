from django.shortcuts import render
from meetings.models import Meeting
from django.http import HttpResponse
from datetime import datetime

# user-jyoti_gupta
#django
def welcome(request):
    return render(request,"website/index.html",{ "meetings":Meeting.objects.all() } )


def about(request):
    return render(request,"website/About.html",{"name":"Jyoti Gupta"})
