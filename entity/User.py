from entity.Artwork import Artwork


class User(Artwork):
    def __init__(self):
        super().__init__()
        self.UserID = 0
        self.Username = ''
        self.Password = ''
        self.Email = ''
        self.FirstName = ''
        self.LastName = ''
        self.DateOfBirth = ''
        self.ProfilePicture = ''
        self.FavoriteArtworks = 0

    # SETTERS
    def set_UserID(self, value):
        self.UserID = value

    def set_Username(self, value):
        self.Username = value

    def set_Password(self, value):
        self.Password = value

    def set_Email(self, value):
        self.Email = value

    def set_FirstName(self, value):
        self.FirstName = value

    def set_LastName(self, value):
        self.LastName = value

    def set_DateOfBirth(self, value):
        self.DateOfBirth = value

    def set_ProfilePicture(self, value):
        self.ProfilePicture = value

    def set_FavoriteArtworks(self, value):
        self.FavoriteArtworks = value

    # GETTERS
    def get_UserID(self):
        return self.UserID

    def get_Username(self):
        return self.Username

    def get_Password(self):
        return self.Password

    def get_Email(self):
        return self.Email

    def get_FirstName(self):
        return self.FirstName

    def get_LastName(self):
        return self.LastName

    def get_DateOfBirth(self):
        return self.DateOfBirth

    def get_ProfilePicture(self):
        return self.ProfilePicture

    def get_FavoriteArtworks(self):
        return self.FavoriteArtworks

    def __str__(self):
        return f'User ID: {self.UserID} Username: {self.Username} Email: {self.Email}\n' \
               f'First Name: {self.FirstName} Last Name: {self.LastName}\n' \
               f'Date of Birth: {self.DateOfBirth} Profile Picture: {self.ProfilePicture}\n' \
               f'Favorite Artworks: {self.FavoriteArtworks}'
