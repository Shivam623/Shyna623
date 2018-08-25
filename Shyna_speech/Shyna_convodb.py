import sqlite3
from Shyna_speech import Shyna_speak


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
    data = (str(key).lower()).translate(str.maketrans({"'": None}))
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

# shyna_get_all()