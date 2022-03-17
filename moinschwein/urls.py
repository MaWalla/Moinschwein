"""moinschwein URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password/', PasswordChangeView.as_view(), name='password'),
    path('live-accusations/', LiveAccusationView.as_view(), name='live_accusations'),
    path('submit-accusation/', SubmitAccusationView.as_view(), name='submit_accusation'),
    path('statistic/global/', StatisticView.as_view(), name='statistic_global'),
    path('statistic/global/data/', StatisticDataView.as_view(), name='statistic_global_data'),
]
