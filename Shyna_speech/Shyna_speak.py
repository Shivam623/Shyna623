from google_speech import Speech
from nltk.tokenize import sent_tokenize
import random


def shyna_speaks(msg: object) -> object:
    msgs=random.choice(msg.split("|"))
    for i in sent_tokenize(msgs):
        print(i)
        lang = "en"
        speech = Speech(i, lang)
        sox_effects = ("speed", "1", )
        speech.play(sox_effects)


def test_shyna_speaks():
    text = "Hey! My name is Shaayna. I have ears and Shiv is working on my eyes. I hope we will see each other soon"
    shyna_speaks(text)


# test_shyna_speaks()