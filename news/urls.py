from django.urls import path

from .api.views import InfoPostView

urlpatterns = [
    path('posts/', InfoPostView.as_view())
]