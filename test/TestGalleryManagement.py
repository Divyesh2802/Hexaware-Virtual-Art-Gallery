import unittest
from dao.GalleryDAO import GalleryDAO
from dao.IVirtualArtGallery import IVirtualArtGallery
import datetime


class TestGalleryManagement(unittest.TestCase):
    # SET UP
    def setUp(self):
        print("Set Up")
        self.obj1 = GalleryDAO()
        self.obj2 = IVirtualArtGallery()

    # TEST GALLERY IS ADDED OR NOT
    def test_add_gallery(self):
        print("test_add_gallery")
        result = self.obj1.add_gallery()
        self.assertEqual(result, True)

    def test_add_gallery_exception(self):
        print("test_add_gallery_exception")
        result = self.obj1.add_gallery()
        self.assertRaises(Exception, result)

    # TEST GALLERY IS UPDATED OR NOT
    def test_update_gallery(self):
        print("test_update_gallery")
        result = self.obj1.update_gallery()
        self.assertEqual(result, True)

    def test_update_gallery_exception(self):
        print("test_update_gallery_exception")
        result = self.obj1.update_gallery()
        self.assertRaises(Exception, result)

    # TEST GALLERY IS DELETED OR NOT
    def test_delete_gallery(self):
        print("test_delete_gallery")
        result = self.obj1.delete_gallery()
        self.assertEqual(result, True)

    def test_delete_gallery_exception(self):
        print("test_delete_gallery_exception")
        result = self.obj1.delete_gallery()
        self.assertRaises(Exception, result)

    # TEST SEARCH GALLERIES FUNCTIONALITY
    def test_searchGalleries(self):
        print("test_searchGalleries")
        result = self.obj2.searchGalleries('Harmony Art Gallery')
        self.assertEqual(result, [(401, 'Harmony Art Gallery', 'Showcasing a diverse range of artworks',
                                   'New York, USA', 101, datetime.timedelta(seconds=64800))])

    def test_searchGalleries_exception(self):
        print("test_searchGalleries_exception")
        result = self.obj2.searchGalleries('Harmony Art Gallery')
        self.assertRaises(Exception, result)

    # TEAR DOWN
    def tearDown(self):
        print("Tear Down")


if __name__ == '__main__':
    unittest.main()
