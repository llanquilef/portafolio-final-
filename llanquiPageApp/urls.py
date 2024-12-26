from rest_framework import routers
from llanquiPageApp import views
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'recomendacionesPersonales', views.R_PersonalViewSet)
router.register(r'recomendacionesUsuario', views.R_UsuarioViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='LlanquiAPI')),
]
