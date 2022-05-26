from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer

class ProductosView(APIView):

    def get(self,request):
        dataProductos = Producto.objects.all()
        serProductos = ProductoSerializer(dataProductos,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)