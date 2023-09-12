from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import RegistrationForm  
from django.views.generic.detail import DetailView
from django.contrib import messages


class SignUpView(CreateView):
    form_class = RegistrationForm  
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('login')
       
   


