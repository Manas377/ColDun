from django.shortcuts import render
from django.http import HttpResponse

from .utility.utility import csv2db

from django.views.generic import TemplateView

# Create your views here.

import pandas as pd
import numpy as np
from django.views.generic import TemplateView
from .models import Company
from .charts import objects_to_df, Chart, get_random_colors

PALETTE = ['#465b65', '#184c9c', '#d33035', '#ffc107', '#28a745', '#6f7f8c', '#6610f2', '#6e9fa5', '#fd7e14', '#e83e8c', '#17a2b8', '#6f42c1' ]



def load_data(request):
    html = "<html><body>DATA LOADED !!!.</body></html>"
    csv2db()
    return HttpResponse(html)

class DataSummary(TemplateView):
    
    def get_context_data(self, **kwargs):
               
        context = super().get_context_data(**kwargs)
        
        
        df = pd.read_csv('data-set/6000_Largest_Companies_ranked_by_Market_Cap.csv') 
        df['marketcaprange'] = pd.cut(df['marketcap'], [0,50000000000, 250000000000, 500000000000, 1000000000000, 3000000000000], labels=['>50B','50-250B','250-500B', '500-1000B', '1000-3000B'])
        df.sort_values(['marketcaprange','marketcap'], ascending=[True, True], inplace=True)
        
        print(df)
        
        context['charts'] = []

        exp_polar = Chart('polarArea', chart_id='polar01', palette=PALETTE)
        exp_polar.from_df(df, values='marketcap', labels=['marketcaprange'])
        context['charts'].append(exp_polar.get_presentation())
        
        unique_countries = df['country'].nunique()

        exp_doughnut = Chart('doughnut', chart_id='doughnut01', palette=get_random_colors(unique_countries))
        exp_doughnut.from_df(df, values='marketcap', labels=['country'])
        context['charts'].append(exp_doughnut.get_presentation())
        

        return context
    

