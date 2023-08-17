from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    
    return render(response, "registry/sign_up.html", {"form":form})

'''
user test:
johndoe, jd@gmail123
janesmith, js@gmail.com, j@ne$m1th!
'''