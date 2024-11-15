from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
from django.utils import timezone

stack = []  # Stack for storage
queue = []  # Queue for storage

def index(request):
    photos = Photo.objects.filter(deleted=False)
    return render(request, 'index.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def delete_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo.deleted = True
    photo.save()
    return redirect('index')

def redo_photo(request):
    deleted_photos = Photo.objects.filter(deleted=True)
    if request.method == 'POST':
        photo_id = request.POST.get('photo_id')
        photo = Photo.objects.get(id=photo_id)
        photo.deleted = False
        photo.save()
        return redirect('index')
    return render(request, 'redo.html', {'deleted_photos': deleted_photos})

# Stack and Queue operations
def stack_view(request):
    global stack
    if request.method == 'POST':
        action = request.POST.get('action')
        value = request.POST.get('value', None)
        if action == 'push' and value:
            stack.append(value)
        elif action == 'pop':
            if stack:
                stack.pop()  # Remove the last item
    return render(request, 'stack_queue.html', {'stack': stack})

def queue_view(request):
    global queue
    if request.method == 'POST':
        action = request.POST.get('action')
        value = request.POST.get('value', None)
        if action == 'enqueue' and value:
            queue.append(value)
        elif action == 'dequeue':
            if queue:
                queue.pop(0)  # Remove the first item
    return render(request, 'stack_queue.html', {'queue': queue})
