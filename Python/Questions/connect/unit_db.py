<<<<<<< HEAD
import unittest
import sqlite3
import connectdb

class test_unit(unittest.TestCase):
    def test_dbconnect(self):
        o=open('data.txt','r')
        r=o.read()
        con=sqlite3.connect('C:\\Users\\DELL\\Desktop\\Questions\\test.db')
        cur=conn.cursor()
        out=connectdb.select(cur)
        set.assertEqual(out,r)

if __name__ == '__main__' :
    unittest.main()
=======
import unittest
import sqlite3
import connectdb

class test_unit(unittest.TestCase):
    def test_dbconnect(self):
        o=open('data.txt','r')
        r=o.read()
        con=sqlite3.connect('C:\\Users\\DELL\\Desktop\\Questions\\test.db')
        cur=conn.cursor()
        out=connectdb.select(cur)
        set.assertEqual(out,r)

if __name__ == '__main__' :
    unittest.main()
>>>>>>> 06ce908d6425d4482fe841a5d13edcee214d17f3
    