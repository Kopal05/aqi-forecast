"""ORM models: one class per database table."""

from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Identity, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from aqi.db.base import Base


class Location(Base):
    """A monitoring station. OpenAQ's ID is kept as a unique external identifier."""

    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    openaq_location_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(Text)
    city: Mapped[str | None] = mapped_column(Text)
    provider: Mapped[str | None] = mapped_column(Text)
    is_monitor: Mapped[bool]
    latitude: Mapped[float | None]
    longitude: Mapped[float | None]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Sensor(Base):
    """One sensor at a location, measuring a single parameter (e.g. PM2.5)."""

    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    openaq_sensor_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    location_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("locations.id"))
    parameter: Mapped[str] = mapped_column(Text)
    units: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class RawMeasurement(Base):
    """One hourly reading from one sensor, stored as received from OpenAQ."""

    __tablename__ = "raw_measurements"

    sensor_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("sensors.id"), primary_key=True)
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    period_end: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    value: Mapped[float]
    coverage_percent: Mapped[float | None]
    has_flags: Mapped[bool | None]
    ingested_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
