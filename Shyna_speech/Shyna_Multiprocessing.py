import multiprocessing
from pocketsphinx import LiveSpeech
import time


def shyna():
    print("This from Shyna the defined function")
    print("This is Shyna who is sleeping", time.sleep(10))


def hey():
    print("This from hey the defined function")
    print("This is hey who is sleeping", time.sleep(10))


if __name__ == '__main__':
    for phrase in LiveSpeech():
        print(phrase)
        if str(phrase).__contains__('HEY'):
            p = multiprocessing.Process(target=hey)
            p.start()
            # p.join()
        elif str(phrase).__contains__('SHYNA'):
            p = multiprocessing.Process(target=shyna)
            p.start()
        else:
            print("I don't know what you said")