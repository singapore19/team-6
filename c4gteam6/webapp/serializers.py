from webapp.models import UserMetadata, ReportData, NewReportData
from rest_framework import serializers

class UserMetadataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users-detail', read_only=True)
    u_timestamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = UserMetadata
        ordering = ['-u_timestamp']
        fields = ('u_timestamp', 'u_name', 'u_age', 'u_gender', 'u_race', 'u_availdays', 'u_availtime', 'url')
        extra_kwargs = {
            'date': {'required': True},
        }

class ReportDataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='reports-detail', read_only=True)
    h_timestamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = ReportData
        ordering = ['-h_timestamp']
        fields = ('h_timestamp', 'h_agerange', 'h_gender', 'h_race', 'h_location', 'h_description', 'url')
        extra_kwargs = {
            'date': {'required': True},
        }

class NewReportDataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='report-detail', read_only=True)
    h_timestamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = NewReportData
        ordering = ['-h_timestamp']
        fields = ('h_timestamp', 'h_location', 'image', 'h_gender', 'h_race', 'h_frequency', 'h_agerange', 'h_description', 'h_risk', 'url')
        extra_kwargs = {
            'date': {'required': True},
        }