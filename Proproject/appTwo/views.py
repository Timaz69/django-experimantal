from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login, logout
from appTwo.models import AccessRecord, Webpage, Topic, Users
from appTwo.forms import FormName, UserForm, UserFormulaire, UserProfilForm
# Create your views here.

def help(request):
    helpdict = {'help_insert' : 'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict   )

def image(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}

    return render(request,'appTwo/image.html', context=date_dict)

def users(request):
    users_list = Users.objects.order_by('last_name')
    lm_dict = {'users_info': users_list}

    return render(request,'appTwo/users.html',context=lm_dict)

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Validation Succes!")
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: '+form.cleaned_data['email'])
            print('TEXT: '+form.cleaned_data['text'])

    return render(request,'appTwo/form_page.html',{'form': form})

def user_form(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return image(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'appTwo/users_sub.html',{'form':form })

def register(request):
    registered = False

    if request.method=='POST':
        user_form = UserFormulaire(data=request.POST)
        profil_form = UserProfilForm(data=request.POST)

        if user_form.is_valid() and profil_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profil = profil_form.save(commit=False)
            profil.user = user

            if 'profil_pic' in request.FILES:
                profil.profil_pic = request.FILES['profil_pic']

            profil.save()
            registered = True

        else:
            print(user_form.errors,profil_form.errors)

    else:
        user_form = UserFormulaire()
        profil_form = UserProfilForm()

    return render(request,'appTwo/registration.html',{'user_form': user_form, 'profil_form': profil_form, 'registered': registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_activate:
                login(request,user)
                return HttpResponseRedirect(reverse('image'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone else  tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,"appTwo/login.html",{})

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('image'))
