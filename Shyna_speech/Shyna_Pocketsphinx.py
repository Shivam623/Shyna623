from pocketsphinx import LiveSpeech
from Shyna_speech import Shyna_convodb
import speech_recognition as sr
'''The start of Speech system is here,'''


def shyna_offline():
    for phrase in LiveSpeech():
        print("offline")
        res = str(phrase)
        print(res)
        if res.__contains__("SHYNA"):
            Shyna_convodb.check_key(res)
            shyna_match()


def shyna_match():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Online")
            audio = r.listen(source, phrase_time_limit=None)
            response = r.recognize_google(audio)
            response.lower()
            print(response)
            shyna_keyword(response)
    except sr.UnknownValueError:
        print("what was that")


def shyna_keyword(res):
    try:
        Shyna_convodb.check_key(res)
    except Exception as e:
        print(e)
    finally:
        shyna_offline()


shyna_offline()