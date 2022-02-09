from django.urls import path
from .import views
appname = 'data'

urlpatterns = [
    path('load/', views.load_data, name = 'load'),
    path('summary/', views.DataSummary.as_view(template_name='data/data-summary.html'), name = 'summary'),
    
]