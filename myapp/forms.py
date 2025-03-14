from django import forms

from myapp.models import Taskmodel

class Userform(forms.Form):

    username = forms.CharField(max_length=60,widget=forms.TextInput(attrs={"class":"form-control","placeholder":" Enetr User Name"}))

    first_name = forms.CharField(max_length=60,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}))

    last_name = forms.CharField(max_length=60,widget=forms.TextInput(attrs={"class":"form-control","placeholder":" Enter Last Name"}))

    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}))




class Login_form(forms.Form):

    username = forms.CharField(max_length=60,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter User Name"}))

    password = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))


class Taskform(forms.ModelForm):

    class Meta:

        model = Taskmodel

        fields = ["task_name","due_data","priority_level"]