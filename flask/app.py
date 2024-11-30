from flask import Flask

app = Flask(__name__)

activities = [
    {

        "activity_id": 10008965,
        "activity_name": "Regent's Park 10 k",
        "total_time": "60:17",
        "lap_times": [
            "10:02"
            "10:00"
            "10:02"
            "10:12"
            "10:00"
            "10:01"
        ]
    }
]

@app.get("/activity")
def get_activity():
    return {"activities": activities}


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

