from django import forms
from appTwo.models import User

class userSignUpForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


# class userSignUpForm(forms.Form):
#     lastName = forms.CharField(max_length=128)
#     firstName = forms.CharField(max_length=128)
#     email = forms.EmailField(max_length=128)
#
#
#     def storeInfo(self):
#         all_clean_data = super().clean()
#         return User.objects.get_or_create(lastName=all_clean_data['lastName'],
#                                    firstName=all_clean_data['firstName'],
#                                    email=all_clean_data['email'])