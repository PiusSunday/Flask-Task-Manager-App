import json
import os

from app.models import Task

DATA_DIR = 'data'

def load_users():
    try:
        with open(os.path.join(DATA_DIR, 'users.txt'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(os.path.join(DATA_DIR, 'users.txt'), 'w') as f:
        json.dump(users, f)

def load_tasks(username):
    try:
        with open(os.path.join(DATA_DIR, f'{username}_tasks.txt'), 'r') as f:
            data = json.load(f)
            return [Task.from_dict(task_data) for task_data in data]
    except FileNotFoundError:
        return []

def save_tasks(username, tasks):
    with open(os.path.join(DATA_DIR, f'{username}_tasks.txt'), 'w') as f:
        json.dump([task.to_dict() for task in tasks], f)