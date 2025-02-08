import os
from django.shortcuts import render
from .forms import UploadFileForm
from .utils.jinja_parser import extract_jinja_statements  # Import skryptu do analizy HTML
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def upload_and_process_file(request):
    result = None
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            file_path = default_storage.save(f"temp/{uploaded_file.name}", ContentFile(uploaded_file.read()))

            # Uruchomienie skryptu
            result = extract_jinja_statements(file_path)

            # Usunięcie tymczasowego pliku
            os.remove(file_path)
    else:
        form = UploadFileForm()

    return render(request, "upload.html", {"form": form, "result": result})
