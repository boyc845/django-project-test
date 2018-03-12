from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.userSignUp_form_view)
]