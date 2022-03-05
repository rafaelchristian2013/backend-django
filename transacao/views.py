from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Transacao
from .serializers import TransacaoSerializer

# Create your views here.

@api_view(['GET'])
def getTransacoes(resquest):
    transacoes = Transacao.objects.all()
    serializer = TransacaoSerializer(transacoes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTransacao(resquest, pk):
    transacoes = Transacao.objects.get(id=pk)
    serializer = TransacaoSerializer(transacoes, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTransacao(request, pk):
    data = request.data
    transacao = Transacao.objects.get(id=pk)
    serializer = TransacaoSerializer(instance=transacao, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createTransacao(request):
    data = request.data
    transacao = Transacao.objects.create(
        body=data['body']
    )
    serializer = TransacaoSerializer(transacao, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTransacao(request, pk):
    transacao = Transacao.objects.get(id=pk)
    transacao.delete()
    return Response('Transacao was deleted!')