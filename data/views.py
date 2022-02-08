from django.shortcuts import render

from .utility.utility import csv2db

from django.views.generic import TemplateView

# Create your views here.


def data_summary(request):
    
    context = {
        
    }
    return render(request, 'data/data-summary.html', context=context)

class DataSummary(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = 'CLASS BASED VIEW'
        
        return context
    

