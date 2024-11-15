from django.urls import path
from .views import index, upload_photo, delete_photo, redo_photo, stack_view, queue_view

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_photo, name='upload_photo'),
    path('delete/<int:photo_id>/', delete
)]