from django.urls import path
from .import views
appname = 'data'

urlpatterns = [
    path('summary/', views.data_summary, name = 'summary'),
]