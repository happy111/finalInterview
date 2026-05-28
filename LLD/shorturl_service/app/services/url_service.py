# File: app/services/url_service.py

from datetime import datetime, timedelta
from app.models import URLMapping
from app.services.id_generator import IDGenerator, Base62Encoder
from app.services.cache import Cache
from app.services.repository import URLRepository

class URLService:
    TTL_YEARS = 5

    def __init__(self):
        self.id_generator = IDGenerator()
        self.encoder = Base62Encoder()
        self.cache = Cache()
        self.repository = URLRepository()

    def create_short_url(self, long_url: str) -> str:
        unique_id = self.id_generator.generate_id()
        short_key = self.encoder.encode(unique_id)

        now = datetime.utcnow()
        mapping = URLMapping(
            short_key=short_key,
            long_url=long_url,
            created_at=now,
            expires_at=now + timedelta(days=365 * self.TTL_YEARS)
        )

        self.repository.save(mapping)
        self.cache.set(short_key, long_url)

        return short_key

    def get_long_url(self, short_key: str) -> str | None:
        long_url = self.cache.get(short_key)
        if long_url:
            return long_url

        mapping = self.repository.find_by_short_key(short_key)
        if not mapping or mapping.expires_at < datetime.utcnow():
            return None

        self.cache.set(short_key, mapping.long_url)
        return mapping.long_url
