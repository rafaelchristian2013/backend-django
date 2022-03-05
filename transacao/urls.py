from django.urls import path
from . import views

urlpatterns = [
    path('transacoes/',views.getTransacoes, name='transacoes'),
    path('transacoes/create/', views.createTransacao, name='create-transacao'),
    path('transacoes/<str:pk>/update/', views.updateTransacao, name='create-transacao'),
    path('transacoes/<str:pk>/delete/', views.deleteTransacao, name='delete-transacao'), 



    path('transacoes/<str:pk>', views.getTransacao, name='transacao'),
]