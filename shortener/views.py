from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from .serializers import urlsSerializer
from .models import urls



# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class urlsViewSet(viewsets.ModelViewSet):
    queryset = urls.objects.all()

    serializer_class = urlsSerializer

