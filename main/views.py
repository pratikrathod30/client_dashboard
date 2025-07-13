from django.shortcuts import render, redirect
from .models import Project, Client, Contact, Subscriber

def landing_page(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    return render(request, 'main/landing.html', {
        'projects': projects,
        'clients': clients,
    })

def submit_contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            city=request.POST.get('city')
        )
    return redirect('landing')

def subscribe(request):
    if request.method == 'POST':
        Subscriber.objects.create(
            email=request.POST.get('email')
        )
    return redirect('landing')
