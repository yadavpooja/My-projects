import unittest
from loginpage import login,register

class Mytest(unittest.TestCase):
    def test_login(self):
        self.assertEqual(login("riya",123,{"riya":123}),0)
    def test_login1(self):
        self.assertEqual(login("riya",233,{"riya":123}),1)
    def test_login2(self):
        self.assertEqual(login("david",233,{"riya":123}),2)
    def test_register1(self):
        self.assertEqual(register("david",321,{"riya":123}),{"riya":123,"david":321})







if __name__ == "__main__":
    unittest.main()
