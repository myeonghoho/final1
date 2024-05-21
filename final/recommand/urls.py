from django.urls import path
from . import views

app_name = "recommand"

urlpatterns = [
    path("", views.main, name="main"),
    path("man/", views.man, name = "man"),  
    path("woman/", views.woman, name = "woman"),  
    path("upload/", views.upload, name = "upload"),
    path("m_ame_1/", views.m_ame_1, name= "m_ame_1"),
    path("m_ame_2/", views.m_ame_2, name= "m_ame_2"),
    path("m_ame_3/", views.m_ame_3, name= "m_ame_3"),
    path("m_ame_4/", views.m_ame_4, name= "m_ame_4"),
    path("m_ame_5/", views.m_ame_5, name= "m_ame_5"),

]