from entity.Artist import Artist


class ArtistDAO(Artist):
    def __init__(self):
        super().__init__()

    def perform_artist_actions(self):
        while True:
            print("(Artist) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_artist_table()
            elif ch == 2:
                print(self.add_artist())
            elif ch == 3:
                print(self.update_artist())
            elif ch == 4:
                print(self.delete_artist())
            elif ch == 5:
                self.select_artist()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_artist_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Artist (
            ArtistID INT PRIMARY KEY,
            Name VARCHAR(50),
            Biography VARCHAR(255),
            BirthDate DATE,
            Nationality VARCHAR(100),
            Website VARCHAR(100),
            ContactInformation VARCHAR(255))'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Artist Table Created successfully.')
        except Exception as e:
            print(e)

    def add_artist(self):
        try:
            self.open()
            self.ArtistID = int(input('Enter Artist ID: '))
            self.Name = input('Enter Name: ')
            self.Biography = input('Enter Biography: ')
            self.BirthDate = input('Enter Birth Date: ')
            self.Nationality = input('Enter Nationality: ')
            self.Website = input('Enter Website: ')
            self.ContactInformation = input('Enter Contact Information: ')
            data = [(self.ArtistID, self.Name, self.Biography, self.BirthDate, self.Nationality, self.Website, self.ContactInformation)]
            insert_str = '''INSERT INTO Artist(ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_artist(self):
        try:
            self.open()
            artist_id = int(input('Input Artist ID to be Updated: '))
            self.Name = input('Enter Name: ')
            self.Biography = input('Enter Biography: ')
            self.BirthDate = input('Enter Birth Date: ')
            self.Nationality = input('Enter Nationality: ')
            self.Website = input('Enter Website: ')
            self.ContactInformation = input('Enter Contact Information: ')
            data = [(self.Name, self.Biography, self.BirthDate, self.Nationality, self.Website, self.ContactInformation, artist_id)]
            update_str = '''UPDATE Artist SET Name=%s, Biography=%s, BirthDate=%s, Nationality=%s, Website=%s, ContactInformation=%s
                            WHERE ArtistID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_artist(self):
        try:
            self.open()
            artist_id = int(input('Input Artist ID to be Deleted: '))
            delete_str = f'''DELETE FROM Artist WHERE ArtistID = {artist_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_artist(self):
        try:
            select_str = '''SELECT * FROM Artist'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Artist Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
