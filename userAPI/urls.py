from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', views.user_list),
    path('add_user', views.add_user),
    path('login', views.login)
]
