from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Ordine, Corriere, Mezzo  
from .forms import OrdineForm, CorriereForm, MezzoForm  

def login_admin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard_admin')
        else:
            return render(request, 'webapp/login.html', {'error': 'Credenziali non valide o non sei staff.'})
    return render(request, 'webapp/login.html')

@staff_member_required
def dashboard_admin_view(request):
    return render(request, 'webapp/dashboard.html')

@staff_member_required
def registrazione_utente_admin_view(request):
    return render(request, 'webapp/registrazione_utente.html')

@staff_member_required
def ordini_admin_view(request):
    if request.method == 'POST':
        form = OrdineForm(request.POST)
        print("Form data:", request.POST)  # Debugging line
        if form.is_valid():
            utente = form.save(commit=False)
        if form.is_valid():
            form.save()
            return redirect('ordini_admin')
    else:
        form = OrdineForm()
    ordini = Ordine.objects.all()
    return render(request, 'webapp/dashboard.html', {'form': form, 'ordini': ordini})

@staff_member_required
def corrieri_admin_view(request):
    if request.method == 'POST':
        form = CorriereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corrieri_admin')
    else:
        form = CorriereForm()
    corrieri = Corriere.objects.all()
    return render(request, 'webapp/corrieri.html', {'form': form, 'corrieri': corrieri})

@staff_member_required
def mezzi_admin_view(request):
    if request.method == 'POST':
        form = MezzoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mezzi_admin')
    else:
        form = MezzoForm()
    mezzi = Mezzo.objects.all()
    return render(request, 'webapp/mezzi.html', {'form': form, 'mezzi': mezzi})
