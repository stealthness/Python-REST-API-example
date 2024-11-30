from flask import Flask, request

app = Flask(__name__)

activities = [
    {

        "activity_id": 10008965,
        "activity_name": "Regent's Park 10 k",
        "total_time": "60:17",
        "lap_times": [
            "10:02",
            "10:00",
            "10:02",
            "10:12",
            "10:00",
            "10:01"
        ]
    }
]

@app.get("/activity")
def get_activity():
    return {"activities": activities}


@app.post("/activity")
def add_activity():
    request_data = request.get_json()
    # new_activity = {
    #     "activity_name": request_data["activity"],
    #     "activity_id": request_data["activity"],
    #     "total_time": request_data["activity"],
    #     "lap_times": request_data["activity"]
    # }
    # activities.append(new_activity)
    return f"You sent: {request_data['activity']['activity_name']}"

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

