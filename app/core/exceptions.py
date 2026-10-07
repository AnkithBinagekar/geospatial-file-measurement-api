class GeospatialAppException(Exception):
    """Base exception for all application-level errors."""
    pass

class UnsupportedFormatError(GeospatialAppException):
    """Raised when an uploaded file format is not supported."""
    pass

class UnknownCRSError(GeospatialAppException):
    """Raised when the Coordinate Reference System cannot be determined."""
    pass

class FileProcessingError(GeospatialAppException):
    """Raised when a failure occurs during file extraction or parsing."""
    pass