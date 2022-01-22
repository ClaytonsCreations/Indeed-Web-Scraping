from .app import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Company = db.Column(db.String(100))
    Location = db.Column(db.String(100))
    Summary = db.Column(db.String(255))
    Post_Date = db.Column(db.String(50))
    Extracted_Date = db.Column(db.String(50))
    Salary = db.Column(db.String(50))

    def __repr__(self):
        return '<Job %r>' % (self.Title)
