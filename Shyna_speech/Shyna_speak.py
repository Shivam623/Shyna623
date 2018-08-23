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
    text = "I’m good|Pretty good|I’m well|I’m OK|Not too bad|Same old, same old|Yeah, all right|I’m alive!"
    shyna_speaks(text)


# test_shyna_speaks()