from django.urls import path
from qa import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.auth_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.auth_logout, name='logout'),
    path('question/<int:id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.pop, name='popular'),
    path('new/', views.test, name='new'),
]