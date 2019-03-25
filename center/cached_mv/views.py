import logging

from rest_framework import viewsets, serializers

from . import models


logger = logging.getLogger(__name__)
logger.debug('this is %s', __name__)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class BelongingSerializer(serializers.ModelSerializer):
    clientId = serializers.IntegerField(source='client.id')

    class Meta:
        model = models.Belonging
        fields = ('id', 'name', 'clientId')

    def validate(self, data):
        """
        Check if clientId exists
        """
        logger.debug('validate is called')
        try:
            client_id = data.pop('client')['id']
            logger.debug(client_id)
            data['client'] = models.Client.objects.get(pk=client_id)
        except models.Client.DoesNotExist:
            raise serializers.ValidationError(F"Given client cannot be found: id={client_id}")
        return data


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = BelongingSerializer