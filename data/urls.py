from django.urls import path

appname = 'data'

urlpatterns = [
    path('summary/', view.data_summary, name = 'summary'),
]