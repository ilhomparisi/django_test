from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
import json
from .models import Item

def index(request):
    return render(request, 'items/index.html')

@require_http_methods(["GET"])
def get_items(request):
    items = Item.objects.all()
    data = []
    for item in items:
        data.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': item.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({'items': data})

@require_http_methods(["POST"])
@csrf_exempt
def create_item(request):
    try:
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data['name'],
            description=data['description']
        )
        return JsonResponse({
            'success': True,
            'item': {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'updated_at': item.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@require_http_methods(["PUT"])
@csrf_exempt
def update_item(request, item_id):
    try:
        data = json.loads(request.body)
        item = Item.objects.get(id=item_id)
        item.name = data['name']
        item.description = data['description']
        item.save()
        return JsonResponse({
            'success': True,
            'item': {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'updated_at': item.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            }
        })
    except Item.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        return JsonResponse({'success': True})
    except Item.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})