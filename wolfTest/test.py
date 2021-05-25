# This file takes the generates string/dict from generate.py and runs it 
# through api.py to recieve wolframs' output. It then calculates the supposed 
# answer to the question (or looks it up in a db is the answer is static) then 
# checks it against the api.py's output

import unittest

class TestStringMethods(unittest.TestCase):

    #test basic addition of two positive numbers
    def test_addition(self):
        self.assertEqual('15+26', '41')

    #test addition of two negative numbers
    def test_addition_negative(self):
        self.assertEqual('-29+-34', '-63')

    #test addition of a positive and negative number
    def test_addition_pos_neg(self):
        self.assertEqual('-57+63', '6')

if __name__ == '__main__':
    unittest.main()
