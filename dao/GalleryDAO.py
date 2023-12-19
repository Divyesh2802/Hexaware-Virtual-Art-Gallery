from entity.Gallery import Gallery


class GalleryDAO(Gallery):
    def __init__(self):
        super().__init__()

    def perform_gallery_actions(self):
        while True:
            print("(Gallery) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")
            ch = int(input("Enter choice: "))
            if ch == 1:
                self.create_gallery_table()
            elif ch == 2:
                print(self.add_gallery())
            elif ch == 3:
                print(self.update_gallery())
            elif ch == 4:
                print(self.delete_gallery())
            elif ch == 5:
                self.select_gallery()
            elif ch == 0:
                break
            else:
                print("Invalid choice")

    def create_gallery_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Gallery (
            GalleryID INT PRIMARY KEY,
            Name VARCHAR(50),
            Description VARCHAR(255),
            Location VARCHAR(50),
            Curator INT,
            OpeningHours TIME,
            FOREIGN KEY(Curator) REFERENCES Artist(ArtistID) ON DELETE CASCADE ON UPDATE CASCADE)'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print('Gallery Table Created successfully.')
        except Exception as e:
            print(e)

    def add_gallery(self):
        try:
            self.open()
            self.GalleryID = int(input('Enter Gallery ID: '))
            self.Name = input('Enter Name: ')
            self.Description = input('Enter Description: ')
            self.Location = input('Enter Location: ')
            self.Curator = int(input('Enter Curator Artist ID: '))
            self.OpeningHours = input('Enter Opening Hours: ')
            data = [(self.GalleryID, self.Name, self.Description, self.Location, self.Curator, self.OpeningHours)]
            insert_str = '''INSERT INTO Gallery(GalleryID, Name, Description, Location, Curator, OpeningHours) 
                            VALUES(%s, %s, %s, %s, %s, %s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def update_gallery(self):
        try:
            self.open()
            gallery_id = int(input('Input Gallery ID to be Updated: '))
            self.Name = input('Enter Name: ')
            self.Description = input('Enter Description: ')
            self.Location = input('Enter Location: ')
            self.Curator = int(input('Enter Curator Artist ID: '))
            self.OpeningHours = input('Enter Opening Hours: ')
            data = [(self.Name, self.Description, self.Location, self.Curator, self.OpeningHours, gallery_id)]
            update_str = '''UPDATE Gallery SET Name=%s, Description=%s, Location=%s, Curator=%s, OpeningHours=%s
                            WHERE GalleryID = %s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def delete_gallery(self):
        try:
            self.open()
            gallery_id = int(input('Input Gallery ID to be Deleted: '))
            delete_str = f'''DELETE FROM Gallery WHERE GalleryID = {gallery_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_gallery(self):
        try:
            select_str = '''SELECT * FROM Gallery'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print('Records In Gallery Table:')
            for i in records:
                print(i)
        except Exception as e:
            print(e)
