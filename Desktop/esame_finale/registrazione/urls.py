from django.contrib import admin
from django.urls import include, path

from dashboard import urls as dashboard_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include(dashboard_urls)), 
    path('login/', 'login.urls'), 
    path('registrazione/', 'registrazione.urls'), 
    path('registrazione_utente/', 'registrazione_utente.urls'), 
]