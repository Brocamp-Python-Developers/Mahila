from django.shortcuts import render
from .models import*
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'user_home/home.html')

def awareness_and_education(request):
    return render(request, 'user_home/awareness_and_education.html')

def support_helpline_section(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone')
        message_text = request.POST.get('message')

        Messages.objects.create(name=name, email=email, phone_no=phone_no, message=message_text)
        messages.success(request, "Your message has been sent")
    
    return render(request, 'user_home/support_helpline_section.html')

def womens_wellness(request):
    return render(request, 'user_home/womens_wellness.html')