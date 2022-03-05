from django.urls import path
from . import views

urlpatterns = [
    path('transacoes/',views.getTransacoes, name='transacoes'),
    path('transacoes/<str:pk>', views.getTransacao, name='transacao')
]