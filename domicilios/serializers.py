from domicilios.models import domiciliarios,clientes
from rest_framework.serializers import ModelSerializer


class domiciliariosSerializer(ModelSerializer):
    class Meta:
        model = domiciliarios
        fields = '__all__'

class clientesSerializer(ModelSerializer):
    class Meta:
        model = clientes
        fields = '__all__'
