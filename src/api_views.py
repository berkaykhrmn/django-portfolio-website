from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Project, Skill, About
from .serializers import ProjectSerializer, SkillSerializer, AboutSerializer

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

class SkillListAPIView(generics.ListAPIView):
    queryset = Skill.objects.all().order_by('name')
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

class AboutAPIView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'  # veya pk