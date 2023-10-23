from django.urls import path
from appTienda import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('categoria',views.CategoriaList.as_view()),
    path('categoria/<int:pk>', views.CategoriaDetail.as_view()),
    path('producto',views.ProductoList.as_view()),
    path('producto/<int:pk>', views.ProductoDetail.as_view()),
    path('productoImagen/',views.ProductoImagen.as_view()),
    path('docs/',include_docs_urls(title='Documentacion API'))
]

