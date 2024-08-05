from rest_framework.decorators import api_view
from restaurante_app.models import Categoria
from api_app.serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def get_categorias(request):
    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.Http_400_BAD_REQUEST)
    elif request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
@api_view(['GET', 'PUT', 'DELETE'])
def categoria_id (request,id):
    if request.method == 'GET':
        try:
            categoria = Categoria.objects.get(id=request.id)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            categoria = Categoria.objects.get(id=request.id)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            categoria = Categoria.objects.get(id=request.id) 
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)