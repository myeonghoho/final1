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

def m_ame_1(request):
    return render(request, "man/man_detail/m_ame/m_americancasual.html")

def m_ame_2(request):
    return render(request, "man/man_detail/m_ame/m_americancasual_2.html")

def m_ame_3(request):
    return render(request, "man/man_detail/m_ame/m_americancasual_3.html")

def m_ame_4(request):
    return render(request, "man/man_detail/m_ame/m_americancasual_4.html")

def m_ame_5(request):
    return render(request, "man/man_detail/m_ame/m_americancasual_5.html")