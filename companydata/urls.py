from django.urls import path
from .import views

app_name = 'companydata'

urlpatterns = [
    path('load/', views.load_data, name = 'load'),
    path('summary/', views.DataSummary.as_view(template_name='companydata/data-summary.html'), name = 'summary'),
    # path('summary/', views.DataSummaryCountry.as_view(template_name='companydata/data-summary.html'), name = 'summary-country'),
    # path('summary/', views.DataSummaryMcap.as_view(template_name='companydata/data-summary.html'), name = 'summary-mcap'),
    
]