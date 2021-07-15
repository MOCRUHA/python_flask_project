from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/side')
def side():
    return render_template('side.html')


if __name__ == '__main__':
    app.run(debug=True)
