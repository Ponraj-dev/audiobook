from ast import excepthandler
import pyttsx3
import PyPDF2
import speech_recognition as sr

listener = sr.Recognizer()
engine =pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)
rate=engine.getProperty("rate")
engine.setProperty("rate",160)


def talk(text):
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
    book=open(file_name,'rb')
    pdfReader =PyPDF2.PdfReader(book)
    pages = pdfReader.numPages
    print(pages)
    for num in range(0,pages):
        page=pdfReader.getPage(0)
        text= page.extractText()
        talk(text)
while True:                  #condition is always true
    try:
        talk("say the file name ")
        read()
    except:
        talk("please type the file name ")
        read(open(input('entre the file name','rb')))
"""except UnknownValueError :
    talk("thank you sir")
    print(" ")"""
