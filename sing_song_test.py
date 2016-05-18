from sing_song import Song, singer
import unittest

class My_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(singer(1),1)

    def test2(self):
        self.assertEqual(singer(2),2)

    def test3(self):
        self.assertEqual(singer(3),3)

    def test4(self):
        self.assertEqual(singer(4),4)

    def test5(self):
        self.assertEqual(singer(5),5)

    def test6(self):
        self.assertEqual(singer(0),0)





if __name__ == "__main__":
    unittest.main()
