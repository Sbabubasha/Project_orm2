from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def data_insertion(request):
    tn=input('enter the topic_name: ')
    Ts=Topic.objects.get_or_create(topic_name=tn)[0]
    Ts.save()
    return HttpResponse('data insertion in Topic is successfull')

def webpage_insertion(request):
    tn=input('enter the topic_name: ')
    na=input('enter the name: ')
    ur=input('enter the url_name: ')
    Ts=Topic.objects.get_or_create(topic_name=tn)[0]
    Ts.save()
    web=Webpage.objects.get_or_create(topic_name=Ts,name=na,url=ur)[0]
    web.save()
    return HttpResponse('Webpage insertion is successfull...!')
def access_insert(request):
    tn=input('enter the topic_name: ')
    na=input('enter the name: ')
    ur=input('enter the url_name: ')
    Ts=Topic.objects.get_or_create(topic_name=tn)[0]
    Ts.save()
    web=Webpage.objects.get_or_create(topic_name=Ts,name=na,url=ur)[0]
    web.save()
    a=input('enter the author: ')
    te=input('enter the date: ')
    ac=Accessrecords.objects.get_or_create(name=web,author=a,date=te)[0]
    ac.save()
    return HttpResponse('Webpage insertion is successfull...!')
