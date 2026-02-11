from django.urls import path
from .views import IndexView
from .api_views import ProjectListCreateAPIView, SkillListAPIView, AboutAPIView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='api-projects'),
    path('api/skills/', SkillListAPIView.as_view(), name='api-skills'),
    path('api/about/<int:id>/', AboutAPIView.as_view(), name='api-about'),
]
