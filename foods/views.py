from django.shortcuts import render
from . import models
def food_list(request):
    food_list = models.Foods.objects.all().order_by('name')
    context = {
        "foods" : food_list
    }
    return render(request, 'foods/home.html', context)

def detail(request , id):
    food_detail = models.Foods.objects.get(id = id)
    context = {
        "food" : food_detail
    }
    return render(request , 'foods/home.html' , context)