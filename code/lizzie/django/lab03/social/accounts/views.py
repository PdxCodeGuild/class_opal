# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    # If I want to add more functionality, have to make my own
    # function that stores all default variables (User.objects.create_user())
    # And probably a forms.py
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"