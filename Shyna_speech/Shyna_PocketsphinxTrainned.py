from pocketsphinx import LiveSpeech, get_model_path, Decoder
from os import path

model_path = get_model_path()
print (model_path)

config = Decoder.default_config()
config.set_string('-hmm', path.join(model_path, 'en-us'))
config.set_string('-lm', path.join(model_path, 'en-us.lm.bin'))
config.set_string('-dict', path.join(model_path, 'cmudict-en-us.dict'))
decoder = Decoder(config)
# print (dir(speech))

for phrase in LiveSpeech():
    print(phrase)