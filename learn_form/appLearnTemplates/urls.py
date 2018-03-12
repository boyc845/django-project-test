from django.urls import path
from appLearnTemplates import views

# Template tagging
app_name = 'appLearnTemplates'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('register/', views.register, name='registeration'),
    path('user_login/', views.user_login, name='user_login')
]