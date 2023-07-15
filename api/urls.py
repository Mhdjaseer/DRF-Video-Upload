from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.vedioUploadView.as_view({'post': 'create', 'get': 'list'}), name='video-upload'),
    path('api/', include('rest_framework.urls')),
]
