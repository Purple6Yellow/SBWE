from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home),
    path('post_list.html/',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
    path('inhoud.html/', views.Inhoud),
    path('index.html/', views.Home),


    path('VerhuurBK.html/', views.VerhuurBK),
        path('ReserveringBK.html/', views.Reservering),
        path('AgendaBK.html/', views.AgendaBK),
        path('Beschikbaarheid.html/', views.Beschikbaarheid),
    path('Fotogalerie.html/', views.Fotogalerie),
    path('Panden.html/', views.Panden),
        path('Rembrandt.html/', views.Rembrandt),
    path('Atelier.html/', views.Ateliers),
    path('Contact.html/', views.Contact),
    path('Historie.html/', views.Historie),
    
    
]