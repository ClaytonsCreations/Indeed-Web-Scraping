from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import indeed_scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    jobs = mongo.db.jobs.find_one()
    return render_template("index.html", jobs=jobs)


@app.route("/scrape")
def scraper():
    jobs = mongo.db.jobs
    jobs_data = indeed_scrape.scrape()
    jobs.update({}, jobs_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)