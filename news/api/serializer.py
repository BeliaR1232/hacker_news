from rest_framework import serializers


from ..models import InfoPost


class InfoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPost
        fields = ('id', 'title', 'url', 'date_created')