from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class MainPaigeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mainapage/mainapage.html')