from django.urls import include, path
from webapp import views
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserMetadataViewSet, base_name='users')
router.register(r'reports', views.ReportDataViewSet, base_name='reports')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('home/', views.index, name='home'),
    path('admin-home/', views.admin_home, name='admin-home'),
    path('submission-form/', views.submission_form, name='submission-form'),
    path('users/<int:pk>/', views.UserMetadataDetail.as_view(), name='users-detail'),
    path('reports/<int:pk>/', views.ReportDataDetail.as_view(), name='reports-detail'),
]