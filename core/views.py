from rest_framework.viewsets import ModelViewSet

from core.models import Marca
from core.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

from core.models import Cores
from core.serializers import CoresSerializer

class CoresViewSet(ModelViewSet):
    queryset = Cores.objects.all()
    serializer_class = CoresSerializer

from core.models import Motores
from core.serializers import MotoresSerializer

class MotoresViewSet(ModelViewSet):
    queryset = Motores.objects.all()
    serializer_class = MotoresSerializer

from core.models import Valor
from core.serializers import ValorSerializer

class ValorViewSet(ModelViewSet):
    queryset = Valor.objects.all()
    serializer_class = ValorSerializer

from core.models import Carro
from core.serializers import CarroSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
