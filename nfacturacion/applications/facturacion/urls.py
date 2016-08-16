from django.conf.urls import url
from .views import FacturacionCreate
from . import views


urlpatterns = [
    #url(r'^$', FacturacionView.as_view()),
    #url(r'^provider/(?P<pk>[-\d]+)/$', ProviderDetailView.as_view()),
    #url(r'^$', ProviderView.as_view()),
    #url(r'^$', ProviderCreateView.as_view()),
    #url(r'^$', FacturacionLista.as_view(), name='facturacion_listar'),
    url(
        r'^provider/$',
        FacturacionCreate.as_view(),
        name='facturacion_create'
    ),
    url(r'^report/$',
        views.ReportListView.as_view(),
        name='reporte'
    ),
]
