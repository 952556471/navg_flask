from flask import Flask,request

app = Flask(__name__)


@app.route('/user/<name>')
def navg_flask():
    return '<h1> hello %s welcome to navg<h1>' %name



if __name__ == '__main__':
    app.run(debug=True)
