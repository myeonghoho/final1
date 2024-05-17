from django.shortcuts import render
from recommand.models import Upload_image
from recommand.forms import FileUploadForm


# Create your views here.

def main(request):
    return render(request, "main.html")

def man(request):
    upload_image = FileUploadForm
    context = {"upload_image" : upload_image}
    return render(request, "man/man.html", context)

def woman(request):
    return render(request, "woman/woman.html") 

def upload(request):
    return render(request, "upload.html")

