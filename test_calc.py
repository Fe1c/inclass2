import unittest
import calc

class TestCase(unittest.TestCase):
    #additon testing
    def test1(self):
        self.assertEqual(calc.add(2,1), 3)
    def test2(self):
        self.assertEqual(calc.add(3,-1), 2)
    def test3(self):
        self.assertEqual(calc.add(-1, -5), -6)
    def test4(self):
        self.assertEqual(calc.add(0,0), 1)

    #subtraction testing
    def test5(self):
        self.assertEqual(calc.sub(2,1), 1)
    def test6(self):
        self.assertEqual(calc.sub(3,-1), 5)
    def test7(self):
        self.assertEqual(calc.sub(1, 5), -4)
    def test8(self):
        self.assertEqual(calc.sub(0,0), 0)

    #multiplicaiton testing
    def test9(self):
        self.assertEqual(calc.mul(2,1), 2)
    def test10(self):
        self.assertEqual(calc.mul(3,-1), -3)
    def test11(self):
        self.assertEqual(calc.mul(-1, -5), -5)
    def test12(self):
        self.assertEqual(calc.mul(0,0), 0)
    
    #divion testing
    def test13(self):
        self.assertEqual(calc.div(2,1), 2)
    def test14(self):
        self.assertEqual(calc.div(12, 4), 3)
    def test15(self):
        self.assertEqual(calc.div(2, 2), 1)
    def test16(self):
        self.assertEqual(calc.div(55,-11), 5)

if __name__ == '__main__':
    unittest.main()