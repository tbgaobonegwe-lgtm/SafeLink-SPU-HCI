from django.contrib import admin
from django.urls import path, include # <--- MUST HAVE 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells the project to look inside your accounts folder
    path('', include('accounts.urls')), 
]