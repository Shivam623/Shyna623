from google_speech import Speech


def shyna_speaks(msg: object) -> object:
    lang = "en"
    speech = Speech(msg, lang)
    sox_effects = ("speed", "1", )
    speech.play(sox_effects)


def test_shyna_speaks():
    text = input("Enter string")
    shyna_speaks(text)


# test_shyna_speaks()