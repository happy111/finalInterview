# File: app/services/repository.py

from app.models import URLMapping

class URLRepository:
    def __init__(self):
        self.db = {}

    def save(self, mapping: URLMapping):
        self.db[mapping.short_key] = mapping

    def find_by_short_key(self, short_key: str):
        return self.db.get(short_key)
