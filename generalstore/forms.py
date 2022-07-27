



from email.policy import default
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from requests import request
from .models import gasentry
from .models import gasondemand





class SignUpForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']

class gasdemand(forms.ModelForm):
    class Meta:
        model=gasondemand
        fields= ['customer_contact','required_quantity','gas_category','customer_address'] 
     

class loginform(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','password']


class newentry(forms.ModelForm):
    class Meta:
        model= gasentry

        # fields= '__all__' 
        fields= ['supplier','quantity', 'category','complete_firm_address', 'firm_contact','Email'] 
        exclude = ('supplier',)
        widgets ={'firm_contact': forms.TextInput(attrs = {
                'placeholder':'(+977)'}  ),
                'complete_firm_address': forms.TextInput(attrs = {'placeholder':'district/city/local area'}  ),
                            
                
                
                }
      