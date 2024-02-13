from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home),
    path('post_list.html/',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
    path('inhoud.html/', views.Inhoud),
    path('index.html/', views.Home),


    path('VerhuurBK.html/', views.VerhuurBK),
        path('Impressie.html/',views.BKImpressie),
        path('ReserveringBK.html/', views.Reservering),
        path('AgendaBK.html/', views.AgendaBK),
        path('Beschikbaarheid.html/', views.Beschikbaarheid),
    path('Panden.html/', views.Panden),
        path('Rembrandt.html/', views.Rembrandt),
        path('Looyer.html/', views.Looyer),
        path('Prinsegracht.html/', views.Prins),
        path('Lepel.html/', views.Lepel),
        path('Barthkapel.html/', views.Barthkapel),

    path('Atelier.html/', views.Ateliers),
    path('Contact.html/', views.Contact),
    path('OverSBWE.html/', views.OverSBWE),
    
    
]