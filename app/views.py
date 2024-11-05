from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        ufs = UF.objects.all()
        return render(request, 'index.html', {'ufs': ufs})
    def post(self, request):
        pass