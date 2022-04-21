# https://www.youtube.com/watch?v=cJveiktaOSQ

from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    # person = {'name':'Dennis', 'age':28}
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    # return Response(person)
    return Response(serializer.data)


# endpoints

@api_view(['POST'])
def addItem(request):
    serializers = ItemSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)