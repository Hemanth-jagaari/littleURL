from django.shortcuts import render
from  django.http import HttpResponse
from .models import URLmap
from django.shortcuts import redirect
from .forms import URL
import random
# Create your views here.
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
        new_url=URLmap(long_url=l_url,short_url=s_url)
        new_url.save()
        short_url='https://pacific-ocean-98235.herokuapp.com/'+s_url
        context={'SHORTURL':short_url,'LONGURL':l_url}
        return render(request,'welcome.html',context)
def urlRedirect(request,sh):
    print("short_url =",sh)
    data=URLmap.objects.get(short_url=sh)
    return redirect(data.long_url)
