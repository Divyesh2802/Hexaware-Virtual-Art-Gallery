from dao.IVirtualArtGallery import IVirtualArtGallery
from dao.ArtistDAO import ArtistDAO
from dao.ArtworkDAO import ArtworkDAO
from dao.UserDAO import UserDAO
from dao.GalleryDAO import GalleryDAO
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException
from util.DBConnUtil import DBConnection


def main():

    dbconnection = DBConnection()

    try:
        dbconnection.open()
        print("--Database Is Connected:--")
    except Exception as e:
        print(e)

    try:
        print("=" * 30)
        print("Virtual Art Gallery")
        print("=" * 30)
        print("Welcome to Virtual Art Gallery!")

        virtual_art_gallery = IVirtualArtGallery()

        while True:
            print("1.Artist 2.Artwork 3.User 4.Gallery 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                a = ArtistDAO()
                a.perform_artist_actions()
            elif ch == 2:
                aw = ArtworkDAO()
                aw.perform_artwork_actions()
            elif ch == 3:
                u = UserDAO()
                u.perform_user_actions()
            elif ch == 4:
                g = GalleryDAO()
                g.perform_gallery_actions()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

        while True:
            print("=" * 10)
            print("---MENU---")
            print("=" * 10)
            print("1.getArtworkById\n2.searchArtworks\n3.addArtworkToFavorite\n4.removeArtworkFromFavorite\n5.getUserFavoriteArtworks\n6.searchGalleries\n0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(virtual_art_gallery.getArtworkById(int(input('Enter Artwork ID to get Artwork Details: '))))
            elif ch == 2:
                print(virtual_art_gallery.searchArtworks(input('Enter Keyword to search Artworks: ')))
            elif ch == 3:
                print(virtual_art_gallery.addArtworkToFavorite(int(input('Enter User ID: ')),
                                                               int(input('Enter Favorite Artwork ID to add: '))))
            elif ch == 4:
                print(virtual_art_gallery.removeArtworkFromFavorite(int(input('Enter User ID: ')),
                                                                    int(input('Enter Favorite Artwork ID to remove: '))))
            elif ch == 5:
                print(virtual_art_gallery.getUserFavoriteArtworks(int(input('Enter User ID to get Favorite Artworks: '))))
            elif ch == 6:
                print(virtual_art_gallery.searchGalleries(input('Enter Keyword to search Galleries: ')))
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    except ArtWorkNotFoundException as e:
        print(e)

    except UserNotFoundException as e:
        print(e)

    except Exception as e:
        print(e)

    finally:
        dbconnection.close()
        print("Thankyou for visiting Virtual Art Gallery!")
        print("--Connection Is Closed:--")


if __name__ == "__main__":
    main()
