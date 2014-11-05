#!/usr/bin/env python


class Triangle():

    def __init__(self):
        self.match = 0
        self.texto = ""
        self.IsATriangle = False

    def setSides(self, a, b, c):
        print "Side A is " + str(a)
        print "Side B is " + str(b)
        print "Side C is " + str(c)
        if (a < b + c) and (b < a + c) and (c < a + b):
            self.IsATriangle = True
        else:
            self.IsATriangle = False

        if self.IsATriangle:
            if (a == b) and (b == c):
                self.texto = "Equilateral"
            elif (a != b) and (a != c) and ( b != c):
                self.texto = "Scalene"
            else:
                self.texto = "Isosceles"
        else:
            self.texto = "Not A Triangle"
        return self.texto
