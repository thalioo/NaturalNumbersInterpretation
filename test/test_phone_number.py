import unittest
import sys,os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from phone_number import PhoneNumber

class TestPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.phone1 = PhoneNumber("0 0 30 69 700 24 1 3 50 2")
        self.phone2 = PhoneNumber("200 20 3 710 4 5")
        self.phone3 = PhoneNumber("2 10 69 30 6 6 4")
        self.phone4 = PhoneNumber("214 65 2 000 1")

    def test_basic(self):
        """
        testing the basic level function

        """
        actual1 = self.phone1.basic()
        expected1 =  ("0030697002413502", "INVALID")

        actual2 = self.phone2.basic()
        expected2 = ("20020371045", "INVALID")

        self.assertEqual(actual1[0], expected1[0])
        self.assertEqual(actual2[1], expected2[1])

    def test_advanced(self):
        """
        Testing of the advanced level using 4 cases
        """
        
        actual1 = self.phone1.advanced()
        expected1 = [("00306972413502", "VALID"),
                        ("0030697241352", "INVALID"),
                        ("0030697002413502", "INVALID"),
                        ("003069700241352", "INVALID"),
                        ("003069720413502", "INVALID"),
                        ("00306972041352", "VALID"),
                        ("0030697002041352", "INVALID"),
                        ("00306970020413502", "INVALID"),
                        ("003060972413502", "INVALID"),
                        ("00306097241352", "INVALID"),
                        ("00306097002413502", "INVALID"),
                        ("0030609700241352", "INVALID"),
                        ("0030609720413502", "INVALID"),
                        ("003060972041352", "INVALID"),
                        ("00306097002041352", "INVALID"),
                        ("003060970020413502", "INVALID")]

        actual2 = self.phone2.advanced()
        expected2 = [
                                ("223700145", "INVALID"),
                                ("2237145", "INVALID"),
                                ("2237001045", "VALID"),
                                ("22371045", "INVALID"),
                                ("22037001045", "INVALID"),
                                ("220371045", "INVALID"),
                                ("2203700145", "VALID"),
                                ("22037145", "INVALID"),
                                ("2002371045", "VALID"),
                                ("20023700145", "INVALID"),
                                ("200237145", "INVALID"),
                                ("200237001045", "INVALID"),
                                ("2002037145", "VALID"),
                                ("20020371045", "INVALID"),
                                ("200203700145", "INVALID"),
                                ("2002037001045", "INVALID"),
                                ]

        actual3 = self.phone3.advanced()
        expected3 = [
                     ("2106930664", "VALID"),
                     ("210693664", "INVALID"),
                     ("21060930664", "INVALID"),
                     ("2106093664", "VALID")
                     ]

        actual4 = self.phone4.advanced()
        expected4 = [("2146520001", "VALID"),
                     ("21460520001", "INVALID"),
                     ("21046520001", "INVALID"),
                     ("210460520001", "INVALID"),
                     ("2001046520001", "INVALID"),
                     ("20010460520001", "INVALID"),
                     ("200146520001", "INVALID"),
                     ("2001460520001", "INVALID")]
        self.assertCountEqual(actual1, expected1)
        self.assertCountEqual(actual2, expected2)
        self.assertCountEqual(actual3, expected3)
        self.assertCountEqual(actual4, expected4)


if __name__ == '__main__':
    unittest.main()
