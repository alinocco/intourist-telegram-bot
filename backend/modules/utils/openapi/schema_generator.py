from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view as default_get_schema_view
from rest_framework.permissions import BasePermission, IsAuthenticated


class _CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = [
            "https",
        ]
        return schema


def get_schema_view(title: str, version: str):
    return default_get_schema_view(
        openapi.Info(title=title, default_version=version),
        public=True,
        generator_class=_CustomSchemaGenerator,
        permission_classes=(IsAuthenticated,)
    )
