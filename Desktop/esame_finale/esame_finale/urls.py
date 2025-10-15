
from django.contrib import admin
from django.urls import path, include 
from login.views import login_view
from dashboard.views import dashboard_view
from registrazione.views import registrazione_view
from registrazione_utente.views import registrazione_utente 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('registrazione/', registrazione_view, name='registrazione'),
    path('registrazione_utente/', registrazione_utente, name='registrazione_utente'),
]
