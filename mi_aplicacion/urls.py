from django.urls import path, include
from mi_aplicacion import views
from rest_framework import routers

#api
router = routers.DefaultRouter()
router.register(r'mi_aplicacion', views.MultasView, 'multas')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('generarMulta/', views.generar_multas)
]