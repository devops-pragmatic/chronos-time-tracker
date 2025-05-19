from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sample(db.Model):
    """
    Example model for demonstration. Replace or extend for your assignment.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


# --- Sample Time Tracker Models ---
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#     time_entries = db.relationship('TimeEntry', backref='project', lazy=True)
#
# class TimeEntry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
#     date = db.Column(db.Date, nullable=False)
#     hours = db.Column(db.Float, nullable=False)
#     notes = db.Column(db.String(256))
# ----------------------------------------------------------------------
