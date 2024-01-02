from django.shortcuts import render
from .models import Menu
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def menu(request):
    menu_data = Menu.objetcs.all()
    main_data = {'menu':menu_data}
    return render(request, 'menu.html', {'menu':main_data})