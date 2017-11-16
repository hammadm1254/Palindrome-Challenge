import palindrome
import unittest
import csv

class TestPalindrome(unittest.TestCase):

    def test_is_Pal(self):
        with self.assertRaises(ValueError):
            palindrome.is_Pal([])
            palindrome.is_Pal(None)
            palindrome.is_Pal('hello')
            palindrome.is_Pal('202')
            palindrome.is_Pal(202)
            palindrome.is_Pal(-202)
        self.assertEqual(palindrome.is_Pal([1]), True)
        self.assertEqual(palindrome.is_Pal([11]), True)
        self.assertEqual(palindrome.is_Pal([00000]), True)
        self.assertEqual(palindrome.is_Pal([123456789]), True)
        self.assertEqual(palindrome.is_Pal([1, 2]), False)
        self.assertEqual(palindrome.is_Pal([1, 0]), False)
        self.assertEqual(palindrome.is_Pal([100, 0, 1010, 999, 1010, 0, 100]), True)
        self.assertEqual(palindrome.is_Pal([100, 0, 1010, 999, 999, 1010, 0, 100]), True)
        self.assertEqual(palindrome.is_Pal([100, 0, 1010, 999, 999, int(1010.001), 0, 100]), True)
        self.assertEqual(palindrome.is_Pal([100, 0, 1010, 999, 999, 1010, 0, str(100)]), False)
        self.assertEqual(palindrome.is_Pal([0, 0, 0, 0, 0, 0]), True)
        self.assertEqual(palindrome.is_Pal([0, 0, 0, 0, 0, 0, 0]), True)
        self.assertEqual(palindrome.is_Pal(palindrome.to_Base(11, 9)), False)
        self.assertEqual(palindrome.is_Pal(palindrome.to_Base(11, 12)), True)

    def test_to_Base(self):
        with self.assertRaises(ValueError):
            ## the type for base is limited to int and value is greater than zero
            ## So for each invalid possiblity of base value we test a valid value
            ## for number input and vice-versa as well as permutations of the two
            ## scenarios

            palindrome.to_Base(0, 0)
            palindrome.to_Base(0, 1)
            palindrome.to_Base(0, -1)
            palindrome.to_Base(0, -9999999999999)
            palindrome.to_Base(0, 2.444)
            palindrome.to_Base(0, str(2))


            palindrome.to_Base(-1, 0)
            palindrome.to_Base(-1, 1)
            palindrome.to_Base(-1, -1)
            palindrome.to_Base(-1, -9999999999999)
            palindrome.to_Base(-1, 2.444)
            palindrome.to_Base(-1, str(2))

            palindrome.to_Base(-9999999991, 2)
            palindrome.to_Base(-1, 2)
            palindrome.to_Base(4.5767, 2)
            palindrome.to_Base(str(100), 2)

        self.assertEqual(palindrome.to_Base(0, 2), [0])
        self.assertEqual(palindrome.to_Base(0, 3), [0])
        self.assertEqual(palindrome.to_Base(0, 999999999999999), [0])
        self.assertEqual(palindrome.to_Base(11, 2), [1, 0, 1, 1])
        self.assertEqual(palindrome.to_Base(11, 3), [1, 0, 2])
        self.assertEqual(palindrome.to_Base(11, 4), [2, 3])
        self.assertEqual(palindrome.to_Base(11, 5), [2, 1])
        self.assertEqual(palindrome.to_Base(11, 6), [1, 5])
        self.assertEqual(palindrome.to_Base(11, 7), [1, 4])
        self.assertEqual(palindrome.to_Base(11, 8), [1, 3])
        self.assertEqual(palindrome.to_Base(11, 9), [1, 2])
        self.assertEqual(palindrome.to_Base(11, 10), [1, 1])
        self.assertEqual(palindrome.to_Base(11, 11), [1, 0])
        self.assertEqual(palindrome.to_Base(11, 12), [11])
        self.assertEqual(palindrome.to_Base(11, 1002), [11])
        self.assertEqual(palindrome.to_Base(1001, 1002), [1001])
        self.assertEqual(palindrome.to_Base(1001, 1000), [1, 1])

    def test_minimum_Base(self):
        with open('testCases.csv', "r") as csv_file:
            reader = csv.reader(csv_file)
            for test in reader:
                if len(test) > 0: # ignores an empty line
                    self.assertEqual(palindrome.minimum_Base(int(test[0])), int(test[1]))

if __name__ == '__main__':
    unittest.main()