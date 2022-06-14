from django.urls import path
from userregistrationapp import views

urlpatterns =[
    path('home/',views.HomeFirstView.as_view(),name='homeuser'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),


    ]