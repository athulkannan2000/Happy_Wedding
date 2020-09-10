from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Gallery
from django.template import loader
from django.http import HttpResponse
from django.template.loader import get_template 


# Create your views here.

def home(request):
	post = Post.objects.all().order_by('-date')
	context={'post':post}
	template = loader.get_template('adam/home.html')
	return HttpResponse(template.render(context, request))
	#return render(request, 'adam/home.html', context)

def login(request):
	context={}
	
	return render(request, 'adam/login.html',context)

def register(request):
	context={}
	if request.methord =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(request, 'adam/login.html')
	else:
		form = UserCreationForm()
	return render(request, 'adam/register.html', {'form':form})

def gallery(request):
	photos = Gallery.objects.all().order_by('-date')
	context={'photos':photos}
	return render(request, 'adam/gallery.html', context)