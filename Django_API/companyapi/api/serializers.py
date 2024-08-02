from rest_framework import serializers
from api.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        # fields = ('name', 'location','about','type','added_date','active')