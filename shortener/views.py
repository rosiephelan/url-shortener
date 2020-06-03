from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .forms import urls_form
from .serializers import urlsSerializer
from .models import urls



# Create your views here.
class HomePageView(TemplateView):

    
    template_name = 'home.html'
    short_url = 'faweubusygbv'

# def post_new(request):
#     if request.method == 'post':
#         form = urls_form(request.POST)
#         if form.is_valid():
#             pass
#         else:
#             return render(request, 'home.html', {'form': form})

class urlsViewSet(viewsets.ModelViewSet):
    queryset = urls.objects.all()

    serializer_class = urlsSerializer

