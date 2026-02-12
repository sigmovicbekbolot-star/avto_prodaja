from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Car
from .serializers import CarSerializer
from .forms import CarForm

# 1. МАШИНА КОШУУ (Жөнөкөй функция)
@login_required
def add_car_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

# 2. БАШКЫ БЕТ (Жөнөкөй функция)
def car_list_view(request):
    query = request.GET.get('q') # Издөө үчүн логика
    if query:
        cars = Car.objects.filter(brand__icontains=query) | Car.objects.filter(model_name__icontains=query)
    else:
        cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/index.html', {'cars': cars})

# 3. РЕГИСТРАЦИЯ (Жөнөкөй функция)
# Көңүл бур! Бул эч кандай класстын ичинде эмес, чекеден башталат!
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cars/register.html', {'form': form})

# 4. REST API (КЛАСС)
class CarListAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'transmission', 'year']
    search_fields = ['title', 'brand', 'model_name']
    ordering_fields = ['price', 'year']