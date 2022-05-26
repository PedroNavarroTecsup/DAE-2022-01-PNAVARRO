from django.urls import path

from . import views

urlpatterns = [
    #path('',views.IndexView.as_view()),
    path('productos',views.ProductosView.as_view()),
    #path('producto/<int:producto_id>',views.ProductoDetailView.as_view())
]