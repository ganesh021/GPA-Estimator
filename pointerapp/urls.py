from django.urls import path
from . import views
urlpatterns = [
    path('',views.start, name='start'),
    path('home',views.home, name='home'),
    path('page',views.page, name='page'),
    path('result', views.main, name='main'),
    path('homecalc', views.homecalc, name='homecalc'),
    path('resultcalc', views.maincalc, name='maincalc'),
    path('about', views.about, name='about'),
    path('contactdeveloper', views.contactdeveloper, name='about'),
    
]