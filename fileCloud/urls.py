"""fileCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from fileUploader.models import User
from fileUploader.views import UserViewSet, register_user
from rest_framework import routers
from django.conf.urls import include
from django.conf.urls import url
#from fileUploader.views import index
#from fileUploader.views import view_books

router = routers.DefaultRouter()
router.register(r'api/user', UserViewSet, base_name='User')
#router.register(r'api/register', register_user)

urlpatterns = [
    url(
        r'^user/$',
        UserViewSet.as_view({'post': 'create'}),
        name='user-create',
    ),
    url(
        r'^user/(?P<string>[\w\-]+)/$',
        TodoViewSet.as_view({'get': 'retrieve'}),
        name='user-retrieve',
    ),
    path('admin/', admin.site.urls),
    path('register/', register_user),
    path(r'', include(router.urls)),
]
