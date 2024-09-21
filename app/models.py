from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    title: str
    description: str
    created_at: datetime = datetime.now()
    completed: bool = False

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):

        task = cls(data['title'], data['description'])
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.completed = data['completed']

        return task