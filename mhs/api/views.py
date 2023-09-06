import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializer import ItemSerializer


# Create your views here.
class ItemView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def get_all_items(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        # print(JsonResponse(serializer.data, safe=False))
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"message": "no get request"}, status=404)


@csrf_exempt
def delete_item(request, id):
    try:
        if request.method == "DELETE":
            try:
                item = Item.objects.get(pk=id)
            except Exception:
                return JsonResponse({"message": "Item not Found"}, status=404)

            item.delete()
            return JsonResponse({"message": "Item deleted successfully"}, status=204)
        else:
            return JsonResponse({"message": "Method not allowed"}, status=404)

    except Exception as e:
        print(f"\n{e}\n")
        return JsonResponse({"message": str(e)}, status=405)


@csrf_exempt
def add_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data["name"]
            price = data["price"]
            type = data["type"]
            brand = data["brand"]

            new_item = Item.objects.create(
                name=name, price=price, type=type, brand=brand
            )

            return JsonResponse(
                {
                    "id": new_item.id,
                    "name": name,
                    "price": price,
                    "type": type,
                    "brand": brand,
                },
                status=200,
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
