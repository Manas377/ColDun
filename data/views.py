from django.shortcuts import render

# Create your views here.


def data_summary(request):
    
    context = {
        
    }
    return render(request, 'data/data-summary.html', context=context)