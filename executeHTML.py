from flask import Flask

app = Flask(__name__)

from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def show_html():
    return send_file('home.html')

if __name__ == '__main__':
    app.run()

