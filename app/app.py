from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from datetime import datetime

from .config import get_database_url
from .models import db, User, Project, TimeEntry

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Initialize database schema on startup
with app.app_context():
    db.create_all()
    # Optionally, populate sample data if the database is empty
    if User.query.count() == 0:
        from .sample_data import populate_sample_data
        populate_sample_data()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return render_template('register.html', error='Username or email already exists.')
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    projects = Project.query.filter_by(user_id=user_id).all()
    time_entries = TimeEntry.query.filter_by(user_id=user_id).all()
    return render_template('user_detail.html', user=user, projects=projects, time_entries=time_entries)

@app.route('/create_project/<int:user_id>', methods=['GET', 'POST'])
def create_project(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        project = Project(name=name, description=description, user_id=user_id)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('user_detail', user_id=user_id))
    return render_template('create_project.html', user=user)

@app.route('/track_time/<int:user_id>', methods=['GET', 'POST'])
def track_time(user_id):
    user = User.query.get_or_404(user_id)
    projects = Project.query.filter_by(user_id=user_id).all()
    if request.method == 'POST':
        project_id = request.form.get('project_id')
        start_time_str = request.form.get('start_time')
        end_time_str = request.form.get('end_time')
        notes = request.form.get('notes')
        start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M') if start_time_str else datetime.now()
        end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M') if end_time_str else None
        duration = int((end_time - start_time).total_seconds()) if end_time else 0
        time_entry = TimeEntry(user_id=user_id, project_id=project_id, start_time=start_time, end_time=end_time, duration=duration, notes=notes)
        db.session.add(time_entry)
        db.session.commit()
        return redirect(url_for('user_detail', user_id=user_id))
    return render_template('track_time.html', user=user, projects=projects)

@app.route('/health')
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
