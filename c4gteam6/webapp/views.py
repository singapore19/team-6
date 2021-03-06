from django.shortcuts import render
from webapp.models import UserMetadata, ReportData, NewReportData
from webapp.serializers import UserMetadataSerializer, ReportDataSerializer, NewReportDataSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, Http404
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

def index(request):
    if request.method == 'GET':
        return render(request, 'home.html')

def admin_home(request):
    if request.method == 'GET':
        return render(request, 'admin-home.html')

def submission_form(request):
    if request.method == 'GET':
        return render(request, 'Submission Form.html')

@csrf_exempt
@api_view(['GET', 'POST'])
def json_form(request):
    if request.method == "POST":
        serializer = NewReportDataSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, 'Submission Form.html')

# Create your views here.
class UserMetadataViewSet(viewsets.ModelViewSet):
    queryset = UserMetadata.objects.all()
    serializer_class = UserMetadataSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'

class UserMetadataDetail(APIView):
    def get_object(self, pk):
        try:
            return UserMetadata.objects.get(pk=pk)
        except UserMetadata.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = UserMetadataSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = UserMetadataSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportDataViewSet(viewsets.ModelViewSet):
    queryset = ReportData.objects.all()
    serializer_class = ReportDataSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'

class ReportDataDetail(APIView):
    """
    Retrieve, update or delete a SermonMetadata instance.
    """
    def get_object(self, pk):
        try:
            return ReportData.objects.get(pk=pk)
        except ReportData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ReportDataSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ReportDataSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NewReportDataViewSet(viewsets.ModelViewSet):
    queryset = NewReportData.objects.all()
    serializer_class = NewReportDataSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'

class NewReportDataDetail(APIView):
    """
    Retrieve, update or delete a SermonMetadata instance.
    """
    def get_object(self, pk):
        try:
            return NewReportData.objects.get(pk=pk)
        except NewReportData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = NewReportDataSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = NewReportDataSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)