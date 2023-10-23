from rest_framework import serializers
from appTienda.models import Categoria, Producto
from drf_extra_fields.fields import Base64ImageField

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'catNombre')

class ProductoSerializer(serializers.ModelSerializer):
    proFoto = Base64ImageField(required=False)

    class Meta:
        model = Producto
        fields = ('id', 'proCodigo','proNombre', 'proPrecio',
                  'proCategoria', 'proFoto')
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'proCodigo','proNombre', 'proPrecio',
                  'proCategoria', 'proFoto')