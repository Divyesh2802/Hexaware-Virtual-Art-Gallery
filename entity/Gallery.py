from entity.Artist import Artist


class Gallery(Artist):
    def __init__(self):
        super().__init__()
        self.GalleryID = 0
        self.Name = ''
        self.Description = ''
        self.Location = ''
        self.Curator = 0
        self.OpeningHours = ''

    # SETTERS
    def set_GalleryID(self, value):
        self.GalleryID = value

    def set_Name(self, value):
        self.Name = value

    def set_Description(self, value):
        self.Description = value

    def set_Location(self, value):
        self.Location = value

    def set_Curator(self, value):
        self.Curator = value

    def set_OpeningHours(self, value):
        self.OpeningHours = value

    # GETTERS
    def get_GalleryID(self):
        return self.GalleryID

    def get_Name(self):
        return self.Name

    def get_Description(self):
        return self.Description

    def get_Location(self):
        return self.Location

    def get_Curator(self):
        return self.Curator

    def get_OpeningHours(self):
        return self.OpeningHours

    def __str__(self):
        return f'Gallery ID: {self.GalleryID} Name: {self.Name}\n' \
               f'Description: {self.Description}\n' \
               f'Location: {self.Location} Curator: {self.Curator} Opening Hours: {self.OpeningHours}'
