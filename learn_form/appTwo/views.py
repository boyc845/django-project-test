from django.shortcuts import render
from appTwo import forms
# Create your views here.
def index(request):
    return render(request, 'basicApp/index.html')


def userSignUp_form_view(request):
    form = forms.userSignUpForm()

    if request.method == "POST":
        form = forms.userSignUpForm(request.POST)
        if form.is_valid():
            print("Validation Success!")
            # print("lastName: " + form.cleaned_data['lastName'])
            # print("firstName: " + form.cleaned_data['firstName'])
            # print("Email: " + form.cleaned_data['email'])
            form.save(commit=True)
            return index(request)
            # result = form.storeInfo()
            # if result[1]:
            #     print("added!")
            #     print("emal: " + str(result[0]))

    form_dict = {"form": form}
    return render(request, 'appTwo/user_sign_up.html', context=form_dict)