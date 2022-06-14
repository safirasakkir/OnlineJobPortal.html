from django.shortcuts import render,redirect
from userregistrationapp.models import User
from userregistrationapp.forms import UserRegistrationForm,LoginForm
from django.views.generic import CreateView,FormView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.
class HomeFirstView(TemplateView):
    template_name = "home.html"
class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('signin')
class SignInView(FormView):
    model = User
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                return render(request, "login.html", {"form": form})
            login(request, user)
            if request.user.is_candidate:
                return redirect("candhome")
            else:
                return redirect("emphome")
