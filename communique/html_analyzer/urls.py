from django.urls import path
from .views import upload_and_process_file

urlpatterns = [
    path("upload/", upload_and_process_file, name="upload"),
]
