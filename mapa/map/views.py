from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Post
import json
# Create your views here.
def map(request):
    return render(request, 'map/map.html')


def save_point(request):
    if request.method == 'POST':
        # Verificar se há dados no corpo da solicitação
        if request.body:
            # Decodificar os dados JSON do corpo da solicitação
            data = json.loads(request.body)
            # Aqui você pode acessar os dados conforme necessário
            print(data)
            # Você pode manipular os dados aqui e, em seguida, retornar uma resposta JSON
            # Exemplo de manipulação de dados:
            response_data = {'status': 'success', 'message': 'Dados recebidos com sucesso'}
            return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'error': 'Método não permitido'})