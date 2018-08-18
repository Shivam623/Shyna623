from pocketsphinx import LiveSpeech
from Shyna_speech import  Shyna_speak
import speech_recognition as sr


def shyna_offline():
    for phrase in LiveSpeech():
        print(type(phrase))
        res = str(phrase)
        print(res)
        if res.__contains__("SHYNA"):
            # print("did you just call me?")
            res = "Shiv!"
            Shyna_speak.shyna_speaks(res)
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("say Something")
                    audio = r.listen(source, phrase_time_limit=None)
                    response = r.recognize_google(audio)
                    # Shyna_speak.shyna_speaks("Yes Query Is Passing")
                    print(response)
                    # return response
            except sr.UnknownValueError:
                print("what was that")


shyna_offline()