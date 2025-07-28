from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),  # Home page view
    #path('login/', views.login_user, name='login'),  # Login view
    path('logout/', views.logout_user, name='logout'),  # Logout view
    path('home/', views.register_user, name='register'),  # Redirect to home view
    path('record/<int:pk>', views.customer_record, name='record'),  # Record view
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),  # Record Delete
    path('add_record/', views.add_record, name='add_record'),  # Record add
    path('update_record/<int:pk>', views.update_record, name='update_record'),  # Record Delete
]
