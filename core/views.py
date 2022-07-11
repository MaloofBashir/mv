from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Registration,Movie
import requests
from . import forms

# Create your views here.

def login(request):
    # if request.method=='POST':
    #     email=request.POST['email']
    #     password=request.POST['password']
    #     user=Registration.objects.get(email=email,password=password)
    #     if user:
    #         print("lol getting")
    #         return redirect('home.html',{'user':user}) 
    return render(request,'login.html')



def signup(request):
    query=None
    exception=None
    try:
        if request.method=="POST":
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            email=request.POST['myemail']
            password=request.POST['mypass']
            query=Registration(first_name=first_name,last_name=last_name,email=email,password=password)
            query.save()
    except Exception as e:
        return HttpResponse("Email already exists")

    return render(request,'singup.html',{'user':query})

def home(request):
    try:
        email=request.POST['email']
        password=request.POST['password']
        user=Registration.objects.get(email=email,password=password)
        request.session['firstname']=user.first_name
        request.session['lastname']=user.last_name
        password=request.POST['password']
        user=Registration.objects.get(email=email,password=password)
        request.session['email']=email
        if user==None:
            redirect("login.html")
        request.session['email']=email
    except Exception as e:
        return HttpResponse("<h2>wrong email or password entered </h2>")
    return render(request,'home.html',{'user':user})

def error(request):
    return render(request,'error.html')

def index(request):
    if request.method=='POST':
        m_name=request.POST['search']
        movies=requests.get("https://www.omdbapi.com/?apikey=706ade06&s="+m_name)
        movies=movies.json()
        movies=movies["Search"]
        return render(request,'index.html',{'mvs':movies})
    
    return redirect('home.html')


def details(request,id):
    return render(request,'details.html')

def addmovie(request):
    if request.method=='POST':
        present_form=forms.MovieList(request.POST)
        if present_form.is_valid():
            try:
                email=request.session['email']
                user=Registration.objects.get(email=email)
                Title=present_form.cleaned_data['Title']
                Year=present_form.cleaned_data['Year']
                Type=present_form.cleaned_data['Type']
                imdbID=present_form.cleaned_data['imdbID']
                Poster=present_form.cleaned_data['Poster']
                Status=present_form.cleaned_data['Status']
                query=Movie(user=user,Title=Title,Year=Year,imdbID=imdbID,Type=Type,Poster=Poster,Status=Status)
                query.save()
            except:
                return HttpResponse("somethign went worng ")
            return HttpResponse("Succefully saved")
            
    else:
        present_form=forms.MovieList()
        return render (request,'addmovie.html',{'form':present_form})


def showall(request):
    try:
        all_objects=Movie.objects.filter(Status='public')
    except:
        return HttpResponse("<h2>something went wrong</h2>")
    return render(request,'showallmovies.html',{'all_movies':all_objects})

def showprivate(request):
    try:
        email=request.session.get('email')
        user=Registration.objects.get(email=email)
        ind_movies=Movie.objects.filter(user=user)
    except:
        return HttpResponse("No availabe movie")
    return render(request,'showprivate.html',{'all_movies':ind_movies})

def logout(request):
    del request.session
    return redirect('login')