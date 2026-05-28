# File: app/models.py

from dataclasses import dataclass
from datetime import datetime

@dataclass
class URLMapping:
    short_key: str
    long_url: str
    created_at: datetime
    expires_at: datetime
