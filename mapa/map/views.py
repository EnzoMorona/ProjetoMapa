from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
# Create your views here.
def map(request):
    return render(request, 'map/map.html')

def save_point(request):
    if request.method == 'POST':
        json = Post.objects.all()
        # Faça o que quiser com as coordenadas, como salvar no banco de dados
        # Por exemplo:
        # Point.objects.create(latitude=latitude, longitude=longitude)
        json.save()
        return render(request, 'map.html', {'json': json})
    else:
        return JsonResponse({'success': False, 'error': 'Método não permitido'})