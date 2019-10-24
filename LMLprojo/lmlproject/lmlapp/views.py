from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'home',
    }
    return render(request, 'normal/home/index.html', context)


def signup(request):
    context = {
        'title': 'Create an account',
    }
    return render(request, 'normal/signup/signup.html',context)


def signin(request):
    return render(request, 'normal/login/login.html')


def employersprofile(request):
    context = {
        'title': 'Company profile',
    }
    return render(request, 'normal/account/employer-profile.html',context)


def employeeprofile(request):
    context = {
        'title': 'Your Profile',
    }
    return render(request, 'normal/account/candidate-profile.html', context)


def employeedetails(request):
    return render(request, 'normal/account/candidate-detail.html')


def companysignup(request):
    return render(request, 'normal/signup/create-company.html')