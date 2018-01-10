from . import models
from django import forms
class Userform(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username','usermail','userpass']
        labels = {'username':"",'usermail':"",'userpass':"",}
        widgets = {'username':forms.TextInput(attrs={'placeholder':'UserName','class':"input_text",'id':'name','name':'username'}),
                   'usermail':forms.EmailInput(attrs={'placeholder':'UserMail','class':"input_text",'id':'mail','name':'usermail',
                    "onchange":"mail_check()"}),
                   'userpass':forms.PasswordInput(attrs={'placeholder':'UserPass','class':"input_text",'id':'pass','name':'userpass'}),
                   }
class Loginform(forms.Form):
    usermail = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input_text'}),label="")
    userpass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Userpass','class':'input_text'}),label="")
