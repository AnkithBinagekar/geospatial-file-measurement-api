import enum
import uuid
from datetime import datetime, timezone
from typing import List, Optional, Any

from sqlalchemy import String, Integer, Float, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class ProcessingStatus(str, enum.Enum):
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

def generate_uuid() -> str:
    return str(uuid.uuid4())

def current_utc_time() -> datetime:
    return datetime.now(timezone.utc)

class FileRecord(Base):
    __tablename__ = "file_records"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=generate_uuid, index=True)
    original_filename: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[ProcessingStatus] = mapped_column(Enum(ProcessingStatus), default=ProcessingStatus.PROCESSING)
    crs: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    feature_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=current_utc_time)
    error_message: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # 1-to-many relationship with features
    features: Mapped[List["Feature"]] = relationship(
        "Feature", back_populates="file_record", cascade="all, delete-orphan"
    )

class Feature(Base):
    __tablename__ = "features"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=generate_uuid, index=True)
    file_id: Mapped[str] = mapped_column(String, ForeignKey("file_records.id"), index=True)
    feature_index: Mapped[int] = mapped_column(Integer, index=True)
    geometry_type: Mapped[str] = mapped_column(String)
    
    # Using JSON for compatibility with GeoJSON representations
    geometry: Mapped[dict[str, Any]] = mapped_column(JSON)
    properties: Mapped[dict[str, Any]] = mapped_column(JSON)
    
    measurement_type: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    measurement_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    measurement_unit: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    # Relationship back to FileRecord
    file_record: Mapped["FileRecord"] = relationship("FileRecord", back_populates="features")