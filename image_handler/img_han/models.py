from django.db import models

# Create your models here.

class Textimg(models.Model):
    img = models.FileField(upload_to='text_photo')
    text = models.TextField(max_length ='200' , blank = True , null = True )

class Tran(models.Model):
    lang = models.TextField(max_length='100')
    tran_text = models.TextField(max_length='2000')


class Voic(models.Model):
    voice_text = models.TextField(max_length='2000')
    voice_lang = models.TextField(max_length='200')
    voice_tran_lang = models.TextField(max_length='200' , null=True , blank = True)
    tran_texte = models.TextField(max_length='2000')
    tran_voice = models.FileField(upload_to='tran_voice')


class Voicesk(models.Model):
    voice_text = models.TextField(max_length='2000')
    voice_lang = models.TextField(max_length='200')
    voice_tran_lang = models.TextField(max_length='200')
    tran_texte = models.TextField(max_length='2000')
    tran_voice = models.FileField(upload_to='text_photo')