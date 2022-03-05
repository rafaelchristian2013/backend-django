from rest_framework.serializers import ModelSerializer
from .models import Transacao

class TransacaoSerializer(ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'