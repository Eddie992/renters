from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate


#A view for creating a new user
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Get the user that was just created
        user = self.object
        # Log the user in
        login(self.request, user, backend='users.backend.EmailPhoneAuthenticationBackend')
        return response

#A view for displaying the home page
class HomeView(TemplateView):
    template_name = 'main.html'

