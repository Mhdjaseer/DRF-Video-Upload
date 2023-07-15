from rest_framework import serializers
from .models import Vedios
from django.conf import settings

class vedio(serializers.ModelSerializer):

    class Meta:
        model = Vedios
        fields = ['id', 'title', 'vedio', 'time']

    def get_url(self, obj):
        request = self.context.get('request')
        if obj.vedio:
            return request.build_absolute_uri(obj.vedio)
        return None
