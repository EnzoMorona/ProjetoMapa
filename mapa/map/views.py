from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def map(request):
    return render(request, 'map/map.html')

def save_point(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        # Faça o que quiser com as coordenadas, como salvar no banco de dados
        # Por exemplo:
        # Point.objects.create(latitude=latitude, longitude=longitude)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método não permitido'})