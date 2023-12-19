from entity.User import User


class UserDAO(User):
    def __init__(self):
        super().__init__()

    def perform_user_actions(self):
        while True:
            print("(User) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_user_table()
            elif ch == 2:
                print(self.add_user())
            elif ch == 3:
                print(self.update_user())
            elif ch == 4:
                print(self.delete_user())
            elif ch == 5:
                self.select_user()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_user_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS User (
            UserID INT PRIMARY KEY,
            Username VARCHAR(50),
            Password VARCHAR(50),
            Email VARCHAR(50),
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            DateOfBirth DATE,
            ProfilePicture VARCHAR(100),
            FavoriteArtworks INT,
            FOREIGN KEY(FavoriteArtworks) REFERENCES Artwork(ArtworkID) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('User Table Created successfully.')
        except Exception as e:
            print(e)

    def add_user(self):
        try:
            self.open()
            self.UserID = int(input('Enter User ID: '))
            self.Username = input('Enter Username: ')
            self.Password = input('Enter Password: ')
            self.Email = input('Enter Email: ')
            self.FirstName = input('Enter First Name: ')
            self.LastName = input('Enter Last Name: ')
            self.DateOfBirth = input('Enter Date of Birth: ')
            self.ProfilePicture = input('Enter Profile Picture: ')
            self.FavoriteArtworks = int(input('Enter Favorite Artwork ID: '))
            data = [(self.UserID, self.Username, self.Password, self.Email, self.FirstName, self.LastName,
                     self.DateOfBirth, self.ProfilePicture, self.FavoriteArtworks)]
            insert_str = '''INSERT INTO User(UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture, FavoriteArtworks) 
                                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_user(self):
        try:
            self.open()
            user_id = int(input('Input User ID to be Updated: '))
            self.Username = input('Enter Username: ')
            self.Password = input('Enter Password: ')
            self.Email = input('Enter Email: ')
            self.FirstName = input('Enter First Name: ')
            self.LastName = input('Enter Last Name: ')
            self.DateOfBirth = input('Enter Date of Birth: ')
            self.ProfilePicture = input('Enter Profile Picture: ')
            self.FavoriteArtworks = int(input('Enter Favorite Artwork ID: '))
            data = [(self.Username, self.Password, self.Email, self.FirstName, self.LastName,
                     self.DateOfBirth, self.ProfilePicture, self.FavoriteArtworks, user_id)]
            update_str = '''UPDATE User SET Username=%s, Password=%s, Email=%s, FirstName=%s, LastName=%s,
                            DateOfBirth=%s, ProfilePicture=%s, FavoriteArtworks=%s
                            WHERE UserID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_user(self):
        try:
            self.open()
            user_id = int(input('Input User ID to be Deleted: '))
            delete_str = f'''DELETE FROM User WHERE UserID = {user_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_user(self):
        try:
            select_str = '''SELECT * FROM User'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In User Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)

    def addArtworkToFavorite(self, user_id, artwork_id):
        pass

    def removeArtworkFromFavorite(self, user_id, artwork_id):
        pass

    def getUserFavoriteArtworks(self, user_id):
        pass
