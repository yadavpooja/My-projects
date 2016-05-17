from distance_cal import dis,Distance
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        self.a = Distance("joy",4,4)
        self.b = dis("dave",2,0)
        self.c = dis("roy","d",2)
        self.d = dis("hary",0,0)
        self.e = dis("hary",4,"w")
        self.f = dis("dove"," ",2)
        self.g = dis("riya",4,4)

    def test_Distance(self):
        self.assertEqual(int(self.a.get_distance()),5)

    def test_dis1(self):
        self.assertEqual(self.b,0)

    def test_dis2(self):
        self.assertEqual(self.c,1)

    def test_dis3(self):
        self.assertEqual(self.d,0)

    def test_dis4(self):
        self.assertEqual(self.e,1)

    def test_dis5(self):
        self.assertEqual(self.f,1)

    def test_dis6(self):
        self.assertEqual(self.g,5)







if __name__ == "__main__":
    unittest.main()
