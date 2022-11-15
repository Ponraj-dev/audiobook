from ast import excepthandler
from distutils.errors import UnknownFileError
import pyttsx3
import PyPDF2
import speech_recognition as sr
import gtts as gt 
import os      
 


listener = sr.Recognizer()
engine =pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)
rate=engine.getProperty("rate")
engine.setProperty("rate",160)


def talk(text):             # function for default voice
    engine.say(text)
    engine.runAndWait()


def read():
    talk("please enter the file name with extension:")
    file_name=input("enter the file name ")
    book=open(file_name,'rb')
    pdfReader =PyPDF2.PdfReader(book)
    pages = pdfReader.numPages
    print(pages)
    for num in range(0,pages):          #loop for read a page wise
        page=pdfReader.getPage(0)
        text= page.extractText()
        print(text)
        letter=text
        voice(letter)
    

def voice(letter):                        #function to read tamil and different languaggesletter
    lang=input("choose the language  :")  #ta-tamil,en-english ....
    tts = gt.gTTS(text=letter, lang=lang)
    tts.save("TamilbookA1.mp3")         # saving file as audio(mp3)
    os.system("TamilbookA1.mp3")        # excuting audio from system
        
        #talk(text)
        #       
try:
    read() #code starts
        
except UnknownFileError :  #if code got an error
    talk("thank you sir")
    print(" ")
