from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('political/', views.political, name='political'),
    path('contact/', views.contact, name='contact'),
    path('breaking/', views.breaking, name='breaking'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('events/', views.events, name='events'),
    path('health/', views.health, name='health'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('shortcodes/', views.shortcodes, name='shortcodes'),
    path('single/', views.single, name='single'),
    path('sports/', views.sports, name='sports'),
    path('technology/', views.technology, name='technology'),
    path('videos/', views.videos, name='videos'),
    path('loginform/', views.loginform, name='loginform'),
    path('Admin/', views.Admn, name='Admn'),
    path('', login, {'template_name': 'website/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.UserFormView.as_view(), name='register'),
]