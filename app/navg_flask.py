from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/user/<name>')
def navg_flask(name):
    return '<h1> hello %s welcome to navg<h1>' %name

@app.route('/test/<name>')
def set_render_template(name):
    return render_template('user.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)
