from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login

def registrazione_utente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cognome = request.POST.get('cognome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'registrazione.html', {'error': 'Le password non coincidono'})

        if User.objects.filter(username=email).exists():
            return render(request, 'registrazione.html', {'error': 'Email già registrata'})

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = nome
        user.last_name = cognome
        user.save()

        login(request, user)
        return redirect('dashboard')

    return render(request, 'registrazione.html')