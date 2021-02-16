import unittest
from romanToInteger import romanToInt

class testRomanInteger(unittest.TestCase):
    
    def test1(self):
        stringtoTest = "III"
        self.assertEqual(3, romanToInt(stringtoTest))
    
    def test2(self):
        stringtoTest = "IV"
        self.assertEqual(4, romanToInt(stringtoTest))

if __name__ == "__main__":
    unittest.main()