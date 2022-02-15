from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = routers.SimpleRouter()
router.register(r'api/messwerts', views.MesswertViewSet)
router.register(r'api/standorts', views.StandortViewSet)


urlpatterns = [
    path('', views.nix, name='index'),
    path('infotext/', views.infotext, name='infotext'),
    path('admin/', views.admin, name='admin'),
    path('<neustereintrag>_<ältestereintrag>', views.neu, name='anderewerte'),
    path('<neustereintrag>%<ältestereintrag>',views.neuer, name='neuer'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),


    #path('index/', views.index, name='detailierter Datenindex'),
]
urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)