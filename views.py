from django.shortcuts import render
from .forms import InfoForm
from .models import InfoModel

# Create your views here.

def home(request):
    if request.method == 'POST':
        #if POST request, validate the data 
        form = InfoForm(request.POST)
        if form.is_valid() and request.POST['phone'].isdigit():
            valid = True
            #if the form is valid, collect the data, submit to db, and thank the user
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            instance=InfoModel(fname=fname, lname=lname, email=email, phone=phone)
            instance.save()
            form = InfoForm()
            return render(request, 'form_db/home.html', {'form':form,'valid':valid})
        
        else:
            valid = False
            form = InfoForm(request.POST)
            return render(request, 'form_db/home.html', {'form':form,'valid':valid})
            
    form = InfoForm()
    return render(request, 'form_db/home.html', {'form':form})
    #if GET request, render page as normal
