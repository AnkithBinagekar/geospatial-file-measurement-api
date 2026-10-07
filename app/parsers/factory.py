class ParserFactory:
    """
    Factory to instantiate the appropriate parser based on file type.
    """
    
    @staticmethod
    def get_parser(filename: str):
        """Stub: Will return ShapefileParser or KMLParser based on extension/MIME."""
        raise NotImplementedError("Parser implementations will be added in Stage 2")