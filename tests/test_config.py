import pytest
from pydantic import ValidationError

from aqi.config import Settings


def test_settings_read_database_url_from_environment(monkeypatch):
    url = "postgresql+psycopg://user:secret@localhost:5432/testdb"
    monkeypatch.setenv("DATABASE_URL", url)

    settings = Settings(_env_file=None)

    assert str(settings.database_url) == url


def test_settings_reject_invalid_database_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "not-a-url")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
