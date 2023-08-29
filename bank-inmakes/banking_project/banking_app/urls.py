from django.urls import path
from . import views
app_name='bank'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout',views.logout,name='logout'),
    path('person-form/', views.person_form, name='person-form'),
    path('get-branches/', views.get_branches, name='get-branches')
    
    
]
