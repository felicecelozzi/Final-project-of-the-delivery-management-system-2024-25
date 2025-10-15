from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'webapp/login.html', {'error': 'Credenziali non valide'})
    return render(request, 'webapp/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'webapp/dashboard.html')

def registrazione_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')  # Usa email come username
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'webapp/registrazione.html', {'error': 'Utente già esistente'})
    return render(request, 'webapp/registrazione.html')

def registrazione_utente_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username=email).exists():
            user = User.objects.create_user(username=email, password=password)
            # Esempio: aggiungi a un gruppo "Corriere"
            gruppo = Group.objects.get(name='Corriere')  # Assicurati che esista
            user.groups.add(gruppo)
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'webapp/registrazione_utente.html', {'error': 'Utente già registrato'})
    return render(request, 'webapp/registrazione_utente.html')
