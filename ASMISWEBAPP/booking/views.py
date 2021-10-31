from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Creating my views here and defining function.
def home(request):
    return render(request, "booking/index.html")  # this will return html instead of http response


def register(request):
    if request.method == "POST":
        username = request.POST['username']  # storing all the fields entered by the user in a variable and
        fname = request.POST['fname']  # request them by post method. (taking the input from the user from backend)
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "username already exist")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request, "Email already exist")
            return redirect('home')
        if len(username) > 10:
            messages.error(request, "Username must be less 10 character")
        if pass1 != pass2:
            messages.error(request, "Password did not match")

        myuser = User.objects.create_user(username, email, pass1)  # creating a user object myuser with
        myuser.first_name = fname  # applicable fields
        myuser.last_name = lname

        myuser.save()  # Saving the user in database
        # shows message to the user when account is created successfully
        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')  # redirects the user to sign page when registration is successful

    return render(request, "booking/register.html")


def signin(request):
    if request.method == 'POST':  # this function takes two parameters(username and password) from the user to them in
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        # this function will authenticate the user to see if the password entered matches with the one in the database

        if user is not None:  # that is, if user is successfully authenticated then login in
            login(request, user)
            fname = user.first_name
            return render(request, "booking/index.html", {'fname': fname})
        #  when authenticated successfully this function will return booking index page along with that a dictionary(content)
        #  is created with first name passed. the welcome message will display like (hello + firstname) as configured in
        #  in the index.html page

        else:  # if user is not authenticated successfully display invalid credential and return to home page
            messages.error(request, "Invalid Credentials")
            return redirect('home')

    return render(request, "booking/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Signed out successfully!")
    return redirect('home')
