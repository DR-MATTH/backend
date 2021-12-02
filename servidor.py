from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def index():
    return '<h3>Hello World!</h3>'


if __name__ == '__main__':
    app.run(debug=True)
