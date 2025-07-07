from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms=[
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Learn Django'},
    {'id': 3, 'name': 'Learn JavaScript'},
    
]
def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request,pk):

    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    context = {'room': room}
            
    return render(request, 'room.html', context)

