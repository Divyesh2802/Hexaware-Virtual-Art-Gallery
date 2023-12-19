from util.DBConnUtil import DBConnection


class Artist(DBConnection):
    def __init__(self):
        super().__init__()
        self.ArtistID = 0
        self.Name = ''
        self.Biography = ''
        self.BirthDate = ''
        self.Nationality = ''
        self.Website = ''
        self.ContactInformation = ''

    # SETTERS
    def set_ArtistID(self, value):
        self.ArtistID = value

    def set_Name(self, value):
        self.Name = value

    def set_Biography(self, value):
        self.Biography = value

    def set_BirthDate(self, value):
        self.BirthDate = value

    def set_Nationality(self, value):
        self.Nationality = value

    def set_Website(self, value):
        self.Website = value

    def set_ContactInformation(self, value):
        self.ContactInformation = value

    # GETTERS
    def get_ArtistID(self):
        return self.ArtistID

    def get_Name(self):
        return self.Name

    def get_Biography(self):
        return self.Biography

    def get_BirthDate(self):
        return self.BirthDate

    def get_Nationality(self):
        return self.Nationality

    def get_Website(self):
        return self.Website

    def get_ContactInformation(self):
        return self.ContactInformation

    def __str__(self):
        return f'Artist ID: {self.ArtistID} Name: {self.Name}\n' \
               f'Biography: {self.Biography} Birth Date: {self.BirthDate} Nationality: {self.Nationality}\n' \
               f' Website: {self.Website} Contact Information: {self.ContactInformation}'
