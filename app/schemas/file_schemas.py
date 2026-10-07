from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Any
from datetime import datetime
from app.db.models import ProcessingStatus

class FileStatusResponse(BaseModel):
    id: str
    original_filename: str
    status: ProcessingStatus
    crs: Optional[str] = None
    feature_count: int
    created_at: datetime
    error_message: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class FeatureMeasurement(BaseModel):
    feature_index: int
    geometry_type: str
    geometry: dict[str, Any]
    properties: dict[str, Any]
    measurement_type: Optional[str] = None
    measurement_value: Optional[float] = None
    measurement_unit: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class PaginatedMeasurementsResponse(BaseModel):
    items: List[FeatureMeasurement]
    total_count: int
    page: int
    size: int
    total_pages: int