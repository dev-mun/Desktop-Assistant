import speech_recognition as sr
import webbrowser
import time
import datetime
import wikipedia
import playsound
import os
import random
from gtts import gTTS
from time import ctime

recognizer = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak("Pardon me, please say that again")
        except sr.RequestError:
            alexis_speak("Sorry, my speech service is down")
        return  voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):

    if 'what is your name' in voice_data:
        alexis_speak("My name is Altrix")

    if 'who are you' in voice_data or 'what can you do' in voice_data:
        alexis_speak('I am Altrix version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube, google chrome, gmail, predict time, get top headline news from CNN')


    if "who made you" in voice_data or "who created you" in voice_data or "who discovered you" in voice_data:
        alexis_speak("I was built by Devish Mundra")


    if 'what time is it' in voice_data:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        alexis_speak("The time is " + current_time)

    if 'search' in voice_data:
        search = record_audio("What do you want to search for?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak("Here is what I found for " + search)

    if 'find location' in voice_data:
        location = record_audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        alexis_speak("Here is the location of " + location)

    if 'play music' in voice_data:
        webbrowser.open_new_tab("https://www.youtube.com")
        alexis_speak("Opening Youtube!")
        time.sleep(5)

    if 'open mail' in voice_data:
        webbrowser.open_new_tab("https://mail.google.com/")
        alexis_speak("Opening Google Mail")
        time.sleep(5)

    if 'news' in voice_data:
        news = webbrowser.open_new_tab("https://us.cnn.com/?hpt=header_edition-picker")
        alexis_speak('Here are some headlines from the CNN,Happy reading')
        time.sleep(6)


    if "stop" in str(voice_data) or "exit" in str(voice_data) or "bye" in str(voice_data):
        alexis_speak("Ok bye take care!")
        exit()

time.sleep(1)
alexis_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)