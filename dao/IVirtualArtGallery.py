from dao.ArtworkDAO import ArtworkDAO
from dao.UserDAO import UserDAO
from dao.GalleryDAO import GalleryDAO
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException


class IVirtualArtGallery(GalleryDAO, ArtworkDAO, UserDAO):
    def __init__(self):
        super().__init__()

    # GET ARTWORK BY ID
    def getArtworkById(self, artwork_id):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Artwork WHERE ArtworkID = {artwork_id}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise ArtWorkNotFoundException(artwork_id)
            else:
                self.stmt.execute(f'''SELECT * FROM Artwork WHERE ArtworkID = {artwork_id}''')
                records = self.stmt.fetchall()
                self.close()
                return records
        except ArtWorkNotFoundException as e:
            return e
        except Exception as e:
            return e

    # SEARCH ARTWORKS
    def searchArtworks(self, keyword):
        try:
            self.open()
            self.stmt.execute(f'''SELECT * FROM Artwork WHERE Title = "{keyword}"''')
            records = self.stmt.fetchall()
            self.close()
            return records
        except Exception as e:
            return e

    # ADD ARTWORK TO FAVORITE
    def addArtworkToFavorite(self, user_id, artwork_id):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Artwork WHERE ArtworkID = {artwork_id}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise ArtWorkNotFoundException(artwork_id)
            self.stmt.execute(f'''SELECT COUNT(*) FROM User WHERE UserID = {user_id}''')
            count2 = self.stmt.fetchone()[0]
            if count2 == 0:
                raise UserNotFoundException(user_id)
            self.stmt.execute(f'''UPDATE User SET FavoriteArtworks = {artwork_id} WHERE UserID = {user_id}''')
            self.conn.commit()
            self.close()
            return True
        except ArtWorkNotFoundException as e:
            print(e)
            return False
        except UserNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

    # REMOVE ARTWORK FROM FAVORITE
    def removeArtworkFromFavorite(self, user_id, artwork_id):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM User WHERE FavoriteArtworks = {artwork_id} AND UserID = {user_id}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise UserNotFoundException(user_id) or ArtWorkNotFoundException(artwork_id)
            self.stmt.execute(f'''DELETE FROM User WHERE FavoriteArtworks = {artwork_id} AND UserID = {user_id}''')
            self.conn.commit()
            self.close()
            return True
        except ArtWorkNotFoundException as e:
            print(e)
            return False
        except UserNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False

    # GET USER FAVORITE ARTWORKS
    def getUserFavoriteArtworks(self, user_id):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM User WHERE UserID = {user_id}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                raise UserNotFoundException(user_id)
            else:
                self.stmt.execute(f'''SELECT U.UserID, AW.* FROM User AS U JOIN Artwork AS AW
                                    ON U.FavoriteArtworks = AW.ArtworkID WHERE UserID = {user_id}''')
                records = self.stmt.fetchall()
                self.close()
                return records
        except UserNotFoundException as e:
            return e
        except Exception as e:
            return e

    # SEARCH GALLERIES
    def searchGalleries(self, keyword):
        try:
            self.open()
            self.stmt.execute(f'''SELECT * FROM Gallery WHERE Name = "{keyword}"''')
            records = self.stmt.fetchall()
            self.close()
            return records
        except Exception as e:
            return e
