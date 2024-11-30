from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <h1>Hello World!</h1>
    <p>This is the homepage</p>
    <p>This is a link to the <a href="/about">About</a> page</p>
    """

@app.route('/about')
def about():
    return """
    <h1>About</h1>
    <p>This is a link to the <a href="/">Home</a> page</p>"""


if __name__ == '__main__':
    app.run(debug=True)

