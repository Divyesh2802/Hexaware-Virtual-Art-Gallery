from entity.Artwork import Artwork


class ArtworkDAO(Artwork):
    def __init__(self):
        super().__init__()

    def perform_artwork_actions(self):
        while True:
            print("(Artwork) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_artwork_table()
            elif ch == 2:
                print(self.add_artwork())
            elif ch == 3:
                print(self.update_artwork())
            elif ch == 4:
                print(self.delete_artwork())
            elif ch == 5:
                self.select_artwork()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_artwork_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Artwork (
            ArtworkID INT PRIMARY KEY,
            Title VARCHAR(50),
            ArtistID INT,
            Description VARCHAR(255),
            CreationDate DATE,
            Medium VARCHAR(100),
            ImageURL VARCHAR(100),
            FOREIGN KEY(ArtistID) REFERENCES Artist(ArtistID) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Artwork Table Created successfully.')
        except Exception as e:
            print(e)

    def add_artwork(self):
        try:
            self.open()
            self.ArtworkID = int(input('Enter Artwork ID: '))
            self.Title = input('Enter Title: ')
            self.ArtistID = int(input('Enter Artist ID: '))
            self.Description = input('Enter Description: ')
            self.CreationDate = input('Enter Creation Date: ')
            self.Medium = input('Enter Medium: ')
            self.ImageURL = input('Enter Image URL: ')
            data = [(self.ArtworkID, self.Title, self.ArtistID, self.Description, self.CreationDate, self.Medium, self.ImageURL)]
            insert_str = '''INSERT INTO Artwork(ArtworkID, Title, ArtistID, Description, CreationDate, Medium, ImageURL) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_artwork(self):
        try:
            self.open()
            artwork_id = int(input('Input Artwork ID to be Updated: '))
            self.Title = input('Enter Title: ')
            self.ArtistID = int(input('Enter Artist ID: '))
            self.Description = input('Enter Description: ')
            self.CreationDate = input('Enter Creation Date: ')
            self.Medium = input('Enter Medium: ')
            self.ImageURL = input('Enter Image URL: ')
            data = [(self.Title, self.ArtistID, self.Description, self.CreationDate, self.Medium, self.ImageURL, artwork_id)]
            update_str = '''UPDATE Artwork SET Title=%s, ArtistID=%s, Description=%s, CreationDate=%s, Medium=%s, ImageURL=%s
                            WHERE ArtworkID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_artwork(self):
        try:
            self.open()
            artwork_id = int(input('Input Artwork ID to be Deleted: '))
            delete_str = f'''DELETE FROM Artwork WHERE ArtworkID = {artwork_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_artwork(self):
        try:
            select_str = '''SELECT * FROM Artwork'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Artwork Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)

    def getArtworkById(self, artwork_id):
        pass

    def searchArtworks(self, keyword):
        pass
