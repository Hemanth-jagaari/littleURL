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
        print(form)
        print("its post")
        s_url=''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for x in range(10))
        #l_url=form.cleaned_dat['url']
        l_url=""
        temp=request.POST.get("LONGURL","")
        print("long url= ",temp)
        l_url=temp
        new_url=URLmap(long_url=l_url,short_url=s_url)
        new_url.save()
        short_url='http://localhost:8000/'+s_url
        #form.instance.SHORTURL=s_url 
        ##request.POST['SHORTURL']=s_url
        context={'SHORTURL':s_url,'LONGURL':l_url}
        return render(request,'welcome.html',context)

        """if form.is_valid():
            s_url=''.join(random.choice(string.ascii_letters) for x in range(10))
            #l_url=form.cleaned_dat['url']
            l_url=""
            temp=request.POS.get("LONGURL","")
            print("long url= ",temp)
            l_url=temp
            new_url=URLmap(long_url=l_url,short_url=s_url)
            new_url.save()
            form.instance.SHORTURL=s_url 
            request.shortURL.add(new_url)
            return redirect(request,'welcome.html',{'SHORTURL':s_url})
        else:
            print(form.errors)
            form=URL()
            data=URLmap.objects.all()
            context={
                'form':form,'data':data
            }
            return render(request,'welcome.html',context)"""
def urlRedirect(request,sh):
    print("short_url =",sh)
    data=URLmap.objects.get(short_url=sh)
    return redirect('https://'+data.long_url)
