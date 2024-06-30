"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from modules.utils.openapi.schema_generator import get_schema_view

admin.autodiscover()

schema_view = get_schema_view(title='Intourist', version='1.0')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/',
        include(
            [
                path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                path('payments/', include('modules.payments.rest.urls')),
                path('signups/', include('modules.signups.rest.urls')),
                path('tours/', include('modules.tours.rest.urls')),
                path('users/', include('modules.users.rest.urls')),
                # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
            ]
        ),
    ),
]
