from django.contrib import admin
from django.urls import path
from . import views
import pybo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('pybo/', pybo.views.pybo_index)
]