from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

#this view handles alot: password hashing / salting, user validation, saving user data to database
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user_profile' #adds a custom name for the user; less generic so it points to the right user

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

