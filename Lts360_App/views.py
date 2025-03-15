from django.shortcuts import render
from django.http import HttpResponse

# View for the homepage
def home(request):
    return render(request, 'lts360/home.html')

# View for the privacy policy page
def privacy_policy(request):
    return render(request, 'lts360/privacy_policy.html')
