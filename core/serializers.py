from rest_framework.serializers import ModelSerializer

from core.models import  Marca, Categoria, Cores, Motores, Valor, Carro

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CoresSerializer(ModelSerializer):
    class Meta:
        model = Cores
        fields = "__all__"

class MotoresSerializer(ModelSerializer):
    class Meta:
        model = Motores
        fields = "__all__"

class ValorSerializer(ModelSerializer):
    class Meta:
        model = Valor
        fields = "__all__"

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"