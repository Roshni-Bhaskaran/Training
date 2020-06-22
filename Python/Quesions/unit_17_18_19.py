import unittest 
import jun17questions
class practice(unittest.TestCase):
    def test_alphanum(self):
        c='a7cc'
        status =jun17questions.alphanum(c)
        self.assertEqual(status,'7')
    def test_long(self):
        m='Roshni'
        status =jun17questions.long(m)
        self.assertEqual(status,"['shn']")
    def test_palindrome(self):
        d=121
        status =jun17questions.palindrome(d)
        self.assertEqual(status,'Palindrome')
    def test_binaryToDecimal(self):
        c=110
        status =jun17questions.binaryToDecimal(c)
        self.assertEqual(status,6)
    def test_mul(self):
        x=[[12,7,3],[4,5,6],[7,8,9]]
        y=[[11,5,6],[5,6,9],[2,9,6]]
        status =jun17questions.mul(x,y)
        self.assertEqual(status,[[173, 129, 153], [81, 104, 105], [135, 164, 168]])
    def test_add(self):
        x=[[12,7,3],[4,5,6],[7,8,9]]
        y=[[11,5,6],[5,6,9],[2,9,6]]
        status =jun17questions.add(x,y)
        self.assertEqual(status,[[23, 12, 9], [9, 11, 15], [9, 17, 15]])
    def test_add_matrix(self):
        a=[[1,2],[4,5]]
        b=[[7,8],[10,11]]
        status =jun17questions.add_matrix(a,b)
        self.assertEqual(status,[[8, 10], [14, 16]])
    def test_mul_matrix(self):
        a=[[1,2],[4,5]]
        b=[[7,8],[10,11]]
        status =jun17questions.mul_matrix(a,b)
        self.assertEqual(status,[[27, 30], [78, 87]])
    
    
        
if __name__ == '__main__': 
    unittest.main() 