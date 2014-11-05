# -*- coding: utf8 -*-
#!/usr/bin/env python

import unittest
from Triangle import Triangle


class Test_Triangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle()

    def test_Triangle_Equilateral(self):
        self.assertEqual("Equilateral", self.triangle.setSides(6, 6, 6))
    def test_Triangle_Scalene(self):
        self.assertEqual("Scalene", self.triangle.setSides(6, 9, 5))
    def test_Triangle_Isosceles(self):
        self.assertEqual("Isosceles", self.triangle.setSides(6, 3, 6))
    def test_Triangle_NotATriangle(self):
        self.assertEqual("Not A Triangle", self.triangle.setSides(5, 5, 12))


if __name__ == "__main__":
    unittest.main()
