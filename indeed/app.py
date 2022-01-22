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
        Title = request.form["Title"]
        Company = request.form["Company"]
        Location = request.form["Location"]
        Summary = request.form["Summary"]
        Post_Date = request.form["Post"]
        Extracted_Date = request.form["Extracted"]
        Salary = request.form["Salary"]

        job = Job(Title=Title, Company=Company, Location=Location, Summary=Summary, Post_Date=Post_Date, Extracted_Date=Extracted_Date, Salary=Salary)
        db.session.add(job)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")



if __name__ == "__main__":
    app.run(debug=True)