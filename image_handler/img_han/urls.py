from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.index , name="home_page"),
    path("voice" , views.voices , name='voice_trasformer')

]