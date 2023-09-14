from django.shortcuts import render

# Create your views here.

def Built_in_Filters(request):
    s='HaI HelLo mY fRiEnD FuCk yOu'
    d={'s':s}
    return render(request, 'Built_in_Filters.html',d)


def Custum_Filter(request):
    d={'s':'HHhai heLLo my ha aAhaFRIEND hai haiIIhai'}
    return render(request, 'Custum_Filter.html',d)