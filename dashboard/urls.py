from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('add_expence',views.add_expense,name='add_expense'),
    path('view_info',views.view_info,name='view_info')

    

]