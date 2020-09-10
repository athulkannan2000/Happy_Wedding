from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# =======
from .models import Post, Gallery
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Post.objects.all().order_by('date')
    return render(request, 'athul/article_list.html', {'articles':articles})

def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return article_list()
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'formName':form})


def signup_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return article_list() # in articles/urls.py: app_name and name in urlpatterns
    else:
        form = UserCreationForm()

    return render(request, 'athul/signup.html', {'formName':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')