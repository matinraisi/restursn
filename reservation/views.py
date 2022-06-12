from django.shortcuts import render

from reservation.forms import Reservform

def login(request):
    login = Reservform()
    if request.method == "POST":
        login = Reservform(request.POST)
        if login.is_valid():
            login.save()
    else:
        login = Reservform()
    context ={
        'form' : login
    }
    return render(request, 'reservation/reservation.html', context)