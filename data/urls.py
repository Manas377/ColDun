from django.urls import path
from .import views
appname = 'data'

urlpatterns = [
    #path('summary/', views.data_summary, name = 'summary'),
    path('summary/', views.DataSummary.as_view(template_name='data/data-summary.html'), name = 'summary'),
    
]