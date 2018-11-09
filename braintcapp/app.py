from flask import Flask
import sqlite3
app = Flask(__name__)


@app.route('/')
def hello():
    con = sqlite3.connect('../db/knowledge_base.db')
    c = con.cursor()
    c.execute("SELECT * FROM knowledge")
    knowledge = c.fetchone()
    print(c.fetchone())
    return "knowledge "+knowledge[1]


if __name__ == '__main__':
    app.run()