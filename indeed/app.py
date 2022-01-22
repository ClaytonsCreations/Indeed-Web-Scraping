import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Job


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        Title = request.form["jobTitle"]
        Company = request.form["jobCo"]
        Summary = request.form["jobSum"]
        Lat = request.form["jobLat"]
        Lon = request.form["jobLong"]
        Salary = request.form["jobSal"]

        job = Job(Title=Title, Company=Company, Lat=Lat, Lon=Lon, Summary=Summary, Salary=Salary)
        db.session.add(job)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")

@app.route("/api/jobs")
def jobs():
    results = db.session.query(Job.Title, Job.Company, Job.Summary, Job.Lat, Job.Lon, Job.Salary).all()

    hover_text = [(result[0],  result[1],  result[5])for result in results]
    lat = [result[3] for result in results]
    lon = [result[4] for result in results]

    job_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(job_data)

if __name__ == "__main__":
    app.run()