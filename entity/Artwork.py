from entity.Artist import Artist


class Artwork(Artist):
    def __init__(self):
        super().__init__()
        self.ArtworkID = 0
        self.Title = ''
        self.ArtistID = 0
        self.Description = ''
        self.CreationDate = ''
        self.Medium = ''
        self.ImageURL = ''

    # SETTERS
    def set_ArtworkID(self, value):
        self.ArtworkID = value

    def set_Title(self, value):
        self.Title = value

    def set_ArtistID(self, value):
        self.ArtistID = value

    def set_Description(self, value):
        self.Description = value

    def set_CreationDate(self, value):
        self.CreationDate = value

    def set_Medium(self, value):
        self.Medium = value

    def set_ImageURL(self, value):
        self.ImageURL = value

    # GETTERS
    def get_ArtworkID(self):
        return self.ArtworkID

    def get_Title(self):
        return self.Title

    def get_ArtistID(self):
        return self.ArtistID

    def get_Description(self):
        return self.Description

    def get_CreationDate(self):
        return self.CreationDate

    def get_Medium(self):
        return self.Medium

    def get_ImageURL(self):
        return self.ImageURL

    def __str__(self):
        return f'Artwork ID: {self.ArtworkID} Title: {self.Title} Artist ID: {self.ArtistID}\n' \
               f'Description: {self.Description} Creation Date: {self.CreationDate} Medium: {self.Medium}\n' \
               f'Image URL: {self.ImageURL}'
