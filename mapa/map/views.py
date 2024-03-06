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
            object = json.loads(request.body)
            data = Post(json = object)
            data.save()
            # Aqui você pode acessar os dados conforme necessário
            print(data)
            # Você pode manipular os dados aqui e, em seguida, retornar uma resposta JSON
            # Exemplo de manipulação de dados:
            response_data = {'status': 'success', 'message': 'Dados recebidos com sucesso'}
            return JsonResponse(response_data)
    else:
        return JsonResponse({'success': False, 'error': 'Método não permitido'})
    

def obter_item(request):
    if request.method == 'GET':
        # Recupere o item do banco de dados (por exemplo, o primeiro item)
        qs_items = Post.objects.all()

        list_items = qs_items.values_list('json', flat=True)

        list_items = [ i for i in list_items ]

        response = json.dumps(list_items)
        # Converta o item para um dicionário ou serialize-o conforme necessário
         # Substitua 'campo1', 'campo2' pelos nomes reais dos campos

        # Retorne o item como uma resposta JSON
        # geojson = {
        #     'type': 'Feature',
        #     'geometry': {
        #         item.geometry
        #     },
        #     'properties': {
        #         'id': item.nome  # Se desejar, você pode adicionar mais propriedades aqui
        #     }
        # }

        # Retorne o GeoJSON como uma resposta JSON
        return JsonResponse(response, safe=False)
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)