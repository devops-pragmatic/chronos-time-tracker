# Sample time tracker data for guidance only.
# You can use this as a reference for your own seed/test data.

sample_projects = [
    {"id": 1, "name": "DevOps Final Project"},
    {"id": 2, "name": "Documentation"},
]

sample_time_entries = [
    {"id": 1, "project_id": 1, "date": "2024-05-20", "hours": 3.5, "notes": "Initial setup and planning."},
    {"id": 2, "project_id": 1, "date": "2024-05-21", "hours": 2.0, "notes": "Docker Compose configuration."},
    {"id": 3, "project_id": 2, "date": "2024-05-21", "hours": 1.0, "notes": "Wrote README and usage docs."},
]

# Example usage (not for production):
# for project in sample_projects:
#     print(project["name"])
