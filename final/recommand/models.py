from django.db import models

# Create your models here.

class Upload_image(models.Model) :
    upload_image = models.ImageField("이미지", upload_to = "media/images/", blank = True)
