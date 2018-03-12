from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    return render(request, 'basicApp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    form_dict = {"form": form}
    return render(request, 'basicApp/form_page.html', context=form_dict)