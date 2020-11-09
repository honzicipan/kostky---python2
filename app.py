from flask import Flask, render_template
import random
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello_world():
    conn = sqlite3.connect("database.db")
    hod = random.randint(1, 6)
    bot_hod = random.randint(1, 6)
    print(hod)
    print(bot_hod)
    c = conn.cursor()
    c.execute("insert into hod values (?, ?)", (bot_hod, hod))
    if(hod > bot_hod):
        c.execute("insert into skore values (1, 0)")
    elif(bot_hod > hod):
        c.execute("insert into skore values (0, 1)")
    else:
        c.execute("insert into skore values (1, 1)")
    c.execute("select sum(hrac), sum(bot) from skore")
    vysledek = c.fetchone()
    conn.commit()
    conn.close()

    return render_template("kostky.html", hod=hod, bhod=bot_hod, vysledek=vysledek)


if __name__ == "__main__":
    app.run()
