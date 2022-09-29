from ast import excepthandler
from distutils.errors import UnknownFileError
import pyttsx3
import PyPDF2
import speech_recognition as sr

#listener = sr.Recognizer()  
engine =pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)    #voice 
rate=engine.getProperty("rate")
engine.setProperty("rate",160)


def talk(text):               #customize pre-define function
    engine.say(text)
    engine.runAndWait()

"""
def file_name():
    with sr.Microphone() as source:
        print("listening....")
        listener.enegrgy_threshold=10000
        listener.adjust_for_ambient_noise(source,1)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower() 
        print(command)"""

def read():
    talk("please enter the file name with extension:")
    file_name=input("enter the file name ")
    book=open(file_name,'rb')                 # readinfg file 
    pdfReader =PyPDF2.PdfReader(book)
    pages = pdfReader.numPages           #number of pages 
    print(pages)
    for num in range(0,pages):
        page=pdfReader.getPage(0)
        text= page.extractText()
        talk(text)
while True:        
    try:
        read()
    
        
    except UnknownFileError :
        talk("thank you sir")
        print(" ")
