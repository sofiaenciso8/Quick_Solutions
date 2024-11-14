from django.shortcuts import render

def mapa_view(request):
    estados = {
        'A1': 1, 'A2': 0, 'A3': 1, 'A4': 0,  # etc.
    }
    return render(request, 'miapp/mapa.html', {'estados': estados})
