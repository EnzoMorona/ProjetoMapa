from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from .models import Post
import json
# Create your views here.
def map(request):
    return render(request, 'map/map.html')


def save_point(request):

    max_instances = 5 

    if request.method == 'POST':
        # Verificar se há dados no corpo da solicitação
        if request.body:
            # Decodificar os dados JSON do corpo da solicitação
            object = json.loads(request.body)
            data = Post(json = object)
            if Post.objects.count() < max_instances:
                data.save()

                response_data = {'status': 'success', 'message': 'Dados recebidos com sucesso'}
                return JsonResponse(response_data)
            else:
                return JsonResponse({'error': 'Limite de instâncias excedido!'}, status=400)


    else:
        return JsonResponse({'success': False, 'error': 'Método não permitido'})
    

def obter_item(request):
    if request.method == 'GET':
        # Recupere o item do banco de dados (por exemplo, o primeiro item)
        qs_items = Post.objects.all()

        list_items = qs_items.values_list('json', flat=True)

        list_items = [ i for i in list_items ]

        response = json.dumps(list_items)

        return JsonResponse(response, safe=False)
    
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)
    

def delete_polygon(request):
    if request.method == 'POST':
        try:
            geojson_data = json.loads(request.body)            
            print(geojson_data)
            # Obtendo todos os polígonos do banco de dados
            db_posts = Post.objects.all()
            id: str
            # Lista para armazenar os valores da chave 'id' dentro dos JSONs
            

            # Iterar sobre todos os objetos Post
            for post in db_posts:
                # Extrair o valor da chave 'id' do JSON e adicioná-lo à lista
                if (post.json['id'] == geojson_data):
                    item_id = post.json
                    post_delete = Post.objects.get(json = item_id)
                    post_delete.delete()
                    print(item_id)
                    
                # Verificando se há uma propriedade de identificação única nos polígonos do GeoJSON


            return JsonResponse({'message': 'Polígonos excluídos com sucesso.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)
