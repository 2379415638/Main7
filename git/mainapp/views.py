from django.shortcuts import render
from . import models
from . import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import random
# Create your views here.
def index(request):
    loginmail = check(request)
    titles = models.Title.objects.all()
    context = {'loginmail':loginmail,'titles':titles}
    return render(request,'index.html',context)
def check(request):
    try:
        loginmail = request.session['loginmail']
    except:
        loginmail = None
    return loginmail
def login(request):
    response = ""
    if request.method == 'POST':
        form = forms.Loginform(data=request.POST)
        if form.is_valid():
            try:
                user = models.User.objects.get(usermail=form.cleaned_data['usermail'])
                if user.userpass == form.cleaned_data['userpass']:
                    request.session['loginmail'] = user.usermail
                    request.session['loginpass'] = user.userpass
                    return HttpResponseRedirect(reverse('main:index'))
                else:
                    response = "×"
            except:
                response = "×"
    else:
        form = forms.Loginform()
    context = {'form':form,'response':response}
    return render(request,'login.html',context)
def logout(request):
    del request.session['loginmail']
    del request.session['loginpass']
    return HttpResponseRedirect(reverse("main:index"))
def user(request):
    loginmail = check(request)
    str = ""
    response = ""
    if request.method == 'POST':
        form = forms.Userform(data=request.POST)
        if int(request.POST['identify']) == request.session['number']:
            if models.User.objects.filter(usermail=request.POST['usermail']).exists():
                response = "×"
            else:
                form.save(commit=1)
                return HttpResponseRedirect(reverse('main:index'))
        else:
            str = "×"
    else:
        try:
            mail = request.session['mail']
            password = request.session['pass']
            name = request.session['name']
            form = forms.Userform(data={'username': name,'usermail': mail,'userpass': password})
            del request.session['mail']
            del request.session['pass']
            del request.session['name']
        except:
            form = forms.Userform()
    context = {'form':form,'str':str,'response':response,'loginmail':loginmail}
    return render(request,'user.html',context)
def send(request,mail,password,name):
    number = random.randint(1000,9999)
    send_mail("Main","Here is the Pass:"+str(number),'postmaster@seeksrq.top',[mail,])
    request.session['number'] = number
    request.session['mail'] = mail
    request.session['pass'] = password
    request.session['name'] = name
    return HttpResponseRedirect(reverse('main:user'))
def content(request,id):
    title = models.Title.objects.get(id = id)
    entries = title.content_set.all()
    context = {'title':title,'entries':entries}
    return render(request, 'entry.html', context)