import sqlite3
from Shyna_speech import Shyna_speak, Remove_punctuation
import random


def notdoundindb(data):
    key = data
    print("I am here")
    conn = sqlite3.connect('test.db')
    conn.execute("INSERT OR IGNORE INTO notfound (key) \
          VALUES (? )", (key,));
    conn.commit()
    print("Records created successfully")
    conn.close()


def createcommandsDB(key, res, func):
    conn = sqlite3.connect('test.db')
    print(type(conn))
    conn.execute("INSERT INTO commands (Keyword,Response,Func) \
      VALUES (?, ?, ? )", (key, res, func));
    conn.commit()
    print("Records created successfully")
    conn.close()


def check_key(key):
    conn = sqlite3.connect('test.db')
    data = Remove_punctuation.remove_punctuation(key)
    print(data)
    try:
        res = None
        cursor = conn.execute("Select response FROM commands WHERE keyword = '"+data+"'");
        # print(cursor)
        cursor=cursor.fetchall()
        for row in cursor:
            res= row[0]
            print(res)
            Shyna_speak.shyna_speaks(res)
        if res == None:
            res = "Not trained on this yet"
            Shyna_speak.shyna_speaks(res)
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print("DB close")


# check_key('how are you')


def shyna_get_all():
    conn = sqlite3.connect('/home/shivam/Documents/Gitdir/Shyna_speech/test.db')
    # data = str(key).lower()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM commands")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)
    finally:
        conn.close()
        print("db Close")


def shyna_for_tele(key):
    print(key, type(key))
    conn = sqlite3.connect('test.db')
    data = Remove_punctuation.remove_punctuation(key)
    print(data)
    try:
        res = None
        cursor = conn.execute("Select response FROM commands WHERE keyword = '" + data + "'");
        print(cursor)
        cursor = cursor.fetchall()
        for row in cursor:
            res = row[0]
            print(res)
            res = random.choice(str(res).split('|'))
            print(res)
            return res
            # Shyna_speak.shyna_speaks(res)
        if res == None:
            print('I ran complete, just passing value')
            a = "Not trained on this yet, I'll inform Shiv, thanks by the way :)|Why every third sentence is a news to " \
                "me, sorry I'll inform to Shiv| Please keep chatting, I am just a kid don't know much :(|Ohkay that " \
                "come out off no where"
            res = random.choice(str(a).split('|'))
            print(res)
            # Shyna_speak.shyna_speaks(res)
            return res
    except Exception as e:
        print(e)
        return 'Ran into an Error it seems!'
    finally:
        conn.close()
        notdoundindb(data)
        print("DB close")


# shyna_for_tele("hahahaha......")
# shyna_get_all()