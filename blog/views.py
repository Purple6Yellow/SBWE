from django.shortcuts import render
from django.utils import timezone 
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Events

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

def Looyer (request):
    return render (request, 'Looyer.html', {})

def Lepel (request):
    return render (request, 'Lepel.html', {})

def Prins (request):
    return render (request, 'Prinsegracht.html', {})

def Barthkapel (request):
    return render (request, 'Barthkapel.html', {})

def Ateliers (request):
    return render (request, 'Atelier.html', {})

def VerhuurBK (request):
    return render (request, 'VerhuurBK.html', {})

def BKImpressie (request):
    return render (request, 'Impressie.html', {})

def Reservering (request):
    return render (request, 'ReserveringBK.html', {})

def AgendaBK (request):
    return render (request, 'AgendaBK.html', {})

def Beschikbaarheid (request):
    return render (request, 'Beschikbaarheid.html', {})

def Contact (request):
    return render (request, 'Contact.html', {})

def OverSBWE (request):
    return render (request, 'OverSBWE.html', {})