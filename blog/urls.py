from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home),
    path('post_list.html/',views.post_list, name='post_list'),
    path('inhoud.html/', views.Inhoud),
    path('index.html/', views.Home),


    path('VerhuurBK.html/', views.VerhuurBK),
        path('ReserveringBK.html/', views.Reservering),
        path('AgendaBK.html/', views.AgendaBK),
    path('Fotogalerie.html/', views.Fotogalerie),
    path('Panden.html/', views.Panden),
    path('Ateliers.html/', views.Ateliers),
    path('Contact.html/', views.Contact),
    
]