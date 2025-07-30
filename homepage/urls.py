from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('verify/<str:token>/',views.verify_email,name='verify_email'),
    path('logout/', views.logout, name='logout'),
    
   
]
