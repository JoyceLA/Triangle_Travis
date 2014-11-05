# -*- coding: utf8 -*-
#!/usr/bin/env python

import unittest
import sys
sys.path.append('../')
from Triangle import Triangle, NumberError


class Test_Triangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle()

    def test_Triangle_Scalene(self):
        self.assertEqual("Scalene", self.triangle.setSides(6, 9, 5))

    def test_Triangle_Isosceles(self):
        self.assertEqual("Isosceles", self.triangle.setSides(6, 3, 6))

    def test_Triangle_Isosceles2(self):
        self.assertEqual("Isosceles", self.triangle.setSides(5, 5, 12))

    def test_Triangle_Isosceles3(self):
        self.assertEqual("Isosceles", self.triangle.setSides(4, 6, 6))

    def test_Triangle_Equilateral(self):
        self.assertEqual("Equilateral", self.triangle.setSides(3, 3, 3))

    def test_Triangle_NotATriangule(self):
        self.assertEqual("NotATriangle", self.triangle.setSides(6, 3, 9))

    def test_Triangle_NotATriangule1(self):
        self.assertEqual("NotATriangle", self.triangle.setSides(12, 7, 5))

    def test_Triangle_NotATriangule2(self):
        self.assertEqual("NotATriangle", self.triangle.setSides(3, 7, 4))

    def test_Triangle_NotATriangule3(self):
        self.assertEqual("NotATriangle", self.triangle.setSides(3, 6, 9))

    def test_Triangle_NotATriangule4(self):
        self.assertEqual("NotATriangle", self.triangle.setSides(6, 12, 6))

    def test_Triangle_NotATriangule5(self):
        self.assertEqual("NotATriangle", self.triangle.setSides(10, 4, 4))

    def test_Triangle_NotATriangule6(self):
        self.assertRaises(NumberError, self.triangle.getMessage(7, 7, -4))


if __name__ == "__main__":
    unittest.main()
