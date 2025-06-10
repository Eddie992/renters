from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from .views import *

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('listing/', include('listings.urls'), name= 'listing'),
    path('', HomeView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),  # Include this last for any other auth views
]