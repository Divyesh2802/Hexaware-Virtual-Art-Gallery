class ArtWorkNotFoundException(Exception):
    def __init__(self, artwork_id):
        super().__init__(f"Artwork ID: {artwork_id} not found in the system.")
