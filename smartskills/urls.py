from django.contrib import admin
from django.urls import path, include
from .views import home, auth, registration, python, django, pyqt5, bootstrap, profile, wrong

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', auth, name='auth'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('courses/bootstrap/', bootstrap, name='bootstrap'),
    path('courses/pyqt5/', pyqt5, name='pyqt5'),
    path('courses/django/', django, name='django'),
    path('courses/python/', python, name='python'),
    path('wrong/', wrong, name='wrong'),
    
    
    
    
]

# Добавьте следующую строку, чтобы подключить представления Django для авторизации и регистрации
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
