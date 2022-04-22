from django import forms

class InfoForm(forms.Form):
    fname = forms.CharField(label = 'First Name:', max_length = 20)
    lname = forms.CharField(label = 'Last Name:', max_length = 20)
    email = forms.EmailField(label = 'Email:', max_length = 100)
    phone = forms.CharField(label = 'Phone:', max_length = 10)