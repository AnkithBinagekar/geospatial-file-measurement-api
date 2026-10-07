from abc import ABC, abstractmethod
from typing import Iterator, Dict, Any, Optional

class BaseParser(ABC):
    """
    Abstract interface for geospatial file format parsers (Shapefile, KML, GeoJSON).
    """
    
    @abstractmethod
    def parse(self, file_path: str) -> Iterator[Dict[str, Any]]:
        """Extracts features one-by-one to avoid high memory usage on large files."""
        pass
        
    @abstractmethod
    def get_crs(self) -> Optional[str]:
        """Returns the native Coordinate Reference System if available."""
        pass