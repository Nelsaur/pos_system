"""pos_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("",views.MenuList,name="list"),
    path("menu/",views.MenuList,name="list"),
    path("menu/<int:pk>/",views.ItemMenuAPIView.as_view(),name="item"),
    path("menu/create/", views.CreateMenuAPIView.as_view(),name="create"),
    path("menu/update/<int:pk>/",views.UpdateMenuAPIView.as_view(),name="update"),
    path("menu/delete/<int:pk>/",views.DeleteMenuAPIView.as_view(),name="delete"),

    path("order/create/", views.CreateOrder, name="create_order"),
    path("order/",views.ListOrderAPIView.as_view(),name="list_order"),
    path("order/<int:pk>/",views.ItemOrderAPIView.as_view(),name="item_order"),
]
