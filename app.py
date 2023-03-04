from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'is this it?'

if __name__ == '__main__':
    app.run(debug=True)     # so you can use in replit with browser in browser: app.run(host='0.0.0.0', deb)
