from leads.models import Lead
from rest_framework import serializers


class LeadSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = '__all__'


