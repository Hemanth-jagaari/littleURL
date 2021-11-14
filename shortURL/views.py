from django.shortcuts import render
from  django.http import HttpResponse
from .models import URLmap,URLmanage
from django.shortcuts import redirect
from .forms import URL
import random
# Create your views here.
n=len('https://pacific-ocean-98235.herokuapp.com/')
def index(request):
    context={}
    print("in index method")
    return render(request,'welcome.html')
def generate_short(request):
    print("in generate method")
    if request.method=='POST':
        form=URL(request.POST)
        print("its post")
        s_url=''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for x in range(10))
        temp=request.POST.get("LONGURL","")
        print("long url= ",temp,"short_url =",s_url)
        l_url=temp
        count=1
        new_url=URLmap(long_url=l_url,short_url=s_url)
        new_url.save()
        dcount=URLmanage(lurl=l_url,surl=s_url,count=count)
        dcount.save()
        print("saved to database url manage")
        short_url='https://pacific-ocean-98235.herokuapp.com/'+s_url
        context={'SHORTURL':short_url,'LONGURL':l_url}
        return render(request,'welcome.html',context)
def urlRedirect(request,sh):
    print("in redirect method" ,len(sh),sh)
    if len(sh)==10:
        data=URLmanage.objects.get(surl=sh)
        dta=URLmap.objects.get(short_url=sh)
        data.count+=1
        data.save()
        return redirect(dta.long_url)
    else:
        return render(request,'welcome.html')
    
    
def get_count(request):
    s_url_data=request.POST.get("scount","")
    s_url=s_url_data[n:]
    print("in get count method",s_url)
    data=URLmanage.objects.get(surl=s_url)
    context={
        'count':data.count,
        'SURL':s_url_data
    }
    return render(request,'welcome.html',context)