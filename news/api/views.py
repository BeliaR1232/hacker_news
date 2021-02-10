from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework_json_api.django_filters import DjangoFilterBackend

from .serializer import InfoPostSerializer
from .pagination import CustomPagination


class InfoPostView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InfoPostSerializer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'url', 'title', 'date_created']
    ordering = ['id']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    @property
    def model(self):
        return self.serializer_class.Meta.model