from django.forms import ModelForm
from recommand.models import Upload_image

class FileUploadForm(ModelForm):
    class Meta:
        model = Upload_image
        fields = ['upload_image']