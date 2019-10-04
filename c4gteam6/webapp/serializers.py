from webapp.models import UserMetadata, ReportData
from rest_framework import serializers

class UserMetadataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users-detail', read_only=True)
    submitTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = UserMetadata
        ordering = ['-submitTime']
        fields = ('submitTime', 'url')
        extra_kwargs = {
            'date': {'required': True},
        }

class ReportDataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='reports-detail', read_only=True)
    submitTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = ReportData
        ordering = ['-submitTime']
        fields = ('submitTime', 'url')
        extra_kwargs = {
            'date': {'required': True},
        }