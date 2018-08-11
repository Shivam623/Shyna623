import speech_recognition as sr
from Shyna_speech import Shyna_speak


def shyna_listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("say Something")
            audio = r.listen(source, phrase_time_limit=None)
            response = r.recognize_google(audio)
            Shyna_speak.shyna_speaks(response)
            print (response)
            return response
    except sr.UnknownValueError:
        print("what was that")
        exit()


shyna_listen()