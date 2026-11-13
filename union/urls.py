"""
URL configuration for union project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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



from union.views import active,duties, first,count,about, hello, members_page
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('members/', members_page),
    path('about/', about),
    path('count/', count),
    path('first/', first),
    path('active/', active),
    path('duties/', duties),
    path("members/<str:name>/", views.member_detail),
    path("duty/<str:duty>/",views.duty_members)
]

