from datetime import datetime, timedelta

from .models import db, User, Project, TimeEntry

def populate_sample_data():
    """Populate the database with sample data for dev/testing."""
    # Clear existing data
    TimeEntry.query.delete()
    Project.query.delete()
    User.query.delete()
    db.session.commit()

    # Sample Users
    user1 = User(username="alice", email="alice@example.com")
    user2 = User(username="bob", email="bob@example.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Sample Projects for Alice
    project1 = Project(name="Website Redesign", description="Redesigning company website", user_id=user1.id)
    project2 = Project(name="Database Migration", description="Migrating database to new server", user_id=user1.id)
    db.session.add(project1)
    db.session.add(project2)
    db.session.commit()

    # Sample Time Entries for Alice
    now = datetime.now()
    entry1 = TimeEntry(
        user_id=user1.id,
        project_id=project1.id,
        start_time=now - timedelta(hours=5),
        end_time=now - timedelta(hours=2),
        duration=10800,  # 3 hours in seconds
        notes="Initial design mockups"
    )
    entry2 = TimeEntry(
        user_id=user1.id,
        project_id=project2.id,
        start_time=now - timedelta(hours=1),
        end_time=None,
        duration=0,
        notes="Setting up new database"
    )
    db.session.add(entry1)
    db.session.add(entry2)
    db.session.commit()

    print("Sample data populated: 2 users, 2 projects, 2 time entries.")
