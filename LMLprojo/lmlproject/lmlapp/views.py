from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'home',
    }
    return render(request, 'normal/home/index.html', context)


def signup(request):

    return render(request, 'normal/signup/signup.html')