from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'user_home/home.html')

def awareness_and_education(request):
    return render(request, 'user_home/awareness_and_education.html')

def support_helpline_section(request):
    return render(request, 'user_home/support_helpline_section.html')