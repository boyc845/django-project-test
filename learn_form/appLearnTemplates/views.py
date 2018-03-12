from django.shortcuts import render
from appLearnTemplates.forms import UserProfileInfoForm, UserForm

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'appLearnTemplates/index.html', context=context_dict)


def other(request):
    return render(request, 'appLearnTemplates/other.html')


def relative(request):
    return render(request, 'appLearnTemplates/relative_url_template.html')


@login_required
def special(request):
    return HttpResponse("You are login")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('appLearnTemplates:index'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.Profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'appLearnTemplates/registration.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('appLearnTemplates:index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
    else:
        return render(request, 'appLearnTemplates/login.html', {})