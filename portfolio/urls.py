"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, routers

from home.views import landing_page, skills_add, skills_edit
# from api import urls


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path("users/", include(router.urls)),
    # path("", landing_page, name="landing_page"),
    path("skills/add/", skills_add, name="skills_add"),
    path("skills/<int:pk>/", skills_edit, name="skills_edit"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

# urlpatterns += urls