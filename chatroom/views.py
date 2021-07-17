from django.shortcuts import redirect, render
from . models import Messages, Room
from django.urls import reverse
from . forms import *

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    room_details = Room.objects.order_by('-date_created')

    context={'room_details':room_details}
    return render(request, 'chatroom/index.html', context)

@login_required(login_url='login')
def roomMessage(request, id):
    room = Room.objects.get(id=id)

    message = Messages.objects.filter(room=id)
    form = MessageForm(initial={'room':room})
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('chatroom:room-message', args=id))
            
    context={'message':message, 'form':form}
    return render(request, 'chatroom/room_message.html', context) 

@login_required(login_url='login')
def createRoom(request, id):
    created_by = User.objects.get(id=id)
    form = RoomForm(initial={'created_by':created_by})

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chatroom:room-home')

    context={'form':form}
    return render(request, 'chatroom/create_room.html', context)      
   

