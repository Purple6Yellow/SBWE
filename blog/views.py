from django.shortcuts import render
from django.utils import timezone 
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render (request, 'post_inhoud.html', { 'post': post})

def Inhoud (request):
    return render (request, 'inhoud.html', {})

def Home (request):
    return render (request, 'index.html', {})

def Panden (request):
    return render (request, 'Panden.html', {})

def Rembrandt (request):
    return render (request, 'Rembrandt.html', {})

def Fotogalerie (request):
    return render (request, 'Fotogalerie.html', {})

def Ateliers (request):
    return render (request, 'Ateliers.html', {})

def VerhuurBK (request):
    return render (request, 'VerhuurBK.html', {})

def Reservering (request):
    return render (request, 'ReserveringBK.html', {})

def AgendaBK (request):
    return render (request, 'AgendaBK.html', {})


def Contact (request):
    return render (request, 'Contact.html', {})