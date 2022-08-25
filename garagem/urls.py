from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import MarcaViewSet

router = DefaultRouter()
router.register(r'marca', MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from core.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from core.views import CoresViewSet

router = DefaultRouter()
router.register(r'cores', CoresViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from core.views import MotoresViewSet

router = DefaultRouter()
router.register(r'motores', MotoresViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from core.views import ValorViewSet

router = DefaultRouter()
router.register(r'valor', ValorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from core.views import CarroViewSet

router = DefaultRouter()
router.register(r'carro', CarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

