from django.shortcuts import render
from .models import *
from PIL import Image
import pytesseract as pt
pt.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from .models import *
from googletrans import Translator
import gtts
# import playsound
# import speech_recognition  as rs

# Create your views here.

def index(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        lang = request.POST.get('lang')
        lang = lang[0:2]
        img1 = Image.open(img)
        # global text
        img_text = pt.image_to_string(img1)
        trans = Translator()
        text = trans.translate(text=img_text , dest=lang)
        text = text.text
        sub = Textimg(img=img , text=text)
        sub.save()
    sub = Textimg.objects.all()
    context ={ 'text':sub}
    return render(request , 'index.html' , context)


def voices(request):
    if request.method == 'POST':
        voice_text= request.POST.get('voice_text')
        voice_lang = request.POST.get('voice_lang')
        voice_tran_lang= request.POST.get('voice_tran_lang')
        # lan = voice_lang
        tran_lan = voice_tran_lang
        tran = Translator()

        text1 = tran.translate(voice_text , dest=tran_lan)

        text_tran = text1.text
        tran_texte = text_tran
        text_voice  = gtts.gTTS(text_tran , lang=tran_lan)
        tran_voice =text_voice.save(f'{voice_lang}.mp3')
        sub  = Voicesk(tran_texte=tran_texte , tran_voice=tran_voice)
        sub.save()
    
    sub3 = Voicesk.objects.all()
    context = {'voc':sub3}
        # play = playsound.playsound('model.mp3')
    return render(request , 'voice.html' , context)