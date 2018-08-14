from pocketsphinx import LiveSpeech
from Shyna_speech import  Shyna_speak


def shyna_offline():
    for phrase in LiveSpeech():
        print(type(phrase))
        res = str(phrase)
        print(res)
        if res == "SHYNA":
            print ("did you just call me?")
            res = "did you just call me?"
            Shyna_speak.shyna_speaks(res)


shyna_offline()