import unittest
from dao.ArtworkDAO import ArtworkDAO
from dao.IVirtualArtGallery import IVirtualArtGallery
import datetime


class TestArtworkManagement(unittest.TestCase):
    # SET UP
    def setUp(self):
        print("Set Up")
        self.obj1 = ArtworkDAO()
        self.obj2 = IVirtualArtGallery()

    # TEST ARTWORK IS ADDED OR NOT
    def test_add_artwork(self):
        print("test_add_artwork")
        result = self.obj1.add_artwork()
        self.assertEqual(result, True)

    def test_add_artwork_exception(self):
        print("test_add_artwork_exception")
        result = self.obj1.add_artwork()
        self.assertRaises(Exception, result)

    # TEST ARTWORK IS UPDATED OR NOT
    def test_update_artwork(self):
        print("test_update_artwork")
        result = self.obj1.update_artwork()
        self.assertEqual(result, True)

    def test_update_artwork_exception(self):
        print("test_update_artwork_exception")
        result = self.obj1.update_artwork()
        self.assertRaises(Exception, result)

    # TEST ARTWORK IS DELETED OR NOT
    def test_delete_artwork(self):
        print("test_delete_artwork")
        result = self.obj1.delete_artwork()
        self.assertEqual(result, True)

    def test_delete_artwork_exception(self):
        print("test_delete_artwork_exception")
        result = self.obj1.delete_artwork()
        self.assertRaises(Exception, result)

    # TEST SEARCH ARTWORKS FUNCTIONALITY
    def test_searchArtworks(self):
        print("test_searchArtworks")
        result = self.obj2.searchArtworks('Portrait of Emotions')
        self.assertEqual(result, [(204, 'Portrait of Emotions', 104, 'Capturing a range of human emotions',
                                   datetime.date(2018, 11, 5), 'Watercolor',
                                   'http://www.example.com/portrait-of-emotions.jpg')])

    def test_searchArtworks_exception(self):
        print("test_searchArtworks_exception")
        result = self.obj2.searchArtworks('Portrait of Emotions')
        self.assertRaises(Exception, result)

    # TEAR DOWN
    def tearDown(self):
        print("Tear Down")


if __name__ == '__main__':
    unittest.main()
