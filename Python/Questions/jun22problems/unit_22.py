import unittest
import jun22
class pract(unittest.TestCase):
    def test_phoneno(self):
        ph='abc99ef67d8992'
        status= jun22.phone(ph)
        self.assertEqual(status,'99678992df')
    def test_one(self):
        s=[1,1,1,0,0,1,1,1,1,1]
        status= jun22.one(s)
        self.assertEqual(status,'11111')
    def test_llist(self):
        l=['1','2','3','4','5','6']
        n=9
        status= jun22.llist(l,n)
        self.assertEqual(status,3) 

if __name__ == '__main__':
    unittest.main()