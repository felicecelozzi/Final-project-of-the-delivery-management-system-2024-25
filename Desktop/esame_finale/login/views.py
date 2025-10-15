from django.urls import path
from django.contrib import admin
from registrazione_utente.views import registrazione_utente
from esame_finale.views import login_view  # <--- assicurati che esista!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrazione/', registrazione_utente, name='registrazione'),
    path('login/', login_view, name='login'),  # <--- login diretto alla view
]
