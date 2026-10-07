from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.models import FileRecord, Feature

class DBRepository:
    """
    Encapsulates all database operations, separating SQL logic from services and routes.
    """
    
    def __init__(self, session: Session):
        self.session = session

    def create_file_record(self, original_filename: str) -> FileRecord:
        record = FileRecord(original_filename=original_filename)
        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)
        return record

    def get_file_record(self, file_id: str) -> Optional[FileRecord]:
        return self.session.get(FileRecord, file_id)

    def save_features(self, features: List[Feature]) -> None:
        self.session.add_all(features)
        self.session.commit()