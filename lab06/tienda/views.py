from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from tienda.carrito import Cart

# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:9]
    cat_list = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'cat_list': cat_list}
    return render(request, 'tienda/index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'tienda/producto.html', {'producto': producto})

def categoria(request, categoria_id):
    product_list = Producto.objects.filter(categoria = categoria_id)[:6]
    cat_list = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'cat_list': cat_list}
    return render(request, 'tienda/categoria.html', context)


def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'tienda/carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'tienda/carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'tienda/carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'tienda/carrito.html')
