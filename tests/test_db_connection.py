import pytest
from sqlalchemy import text

from aqi.db.session import get_engine


@pytest.mark.integration
def test_database_connection():
    with get_engine().connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar_one() == 1