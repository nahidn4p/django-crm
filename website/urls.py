from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),  # Home page view
    #path('login/', views.login_user, name='login'),  # Login view
    path('logout/', views.logout_user, name='logout'),  # Logout view
    path('home/', views.register_user, name='register'),  # Redirect to home view
]
