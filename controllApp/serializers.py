
from rest_framework.serializers import ModelSerializer
from .models import *

class DataSerialize(ModelSerializer):

    class Meta:
        model = all#User,Document,Agence,Client,Document,Historique,Lignedocument
        fields= '__all__'