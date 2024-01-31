from django import forms  


class loginform(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class signupform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    c_password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class upload_f(forms.Form):
    r_email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    
