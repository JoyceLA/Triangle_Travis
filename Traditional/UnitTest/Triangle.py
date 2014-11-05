#!/usr/bin/env python


class Triangle():

    def __init__(self):
        self.match = 0
        self.texto = ""

    def setSides(self, a, b, c):
        print "Side A is " + str(a)
        print "Side B is " + str(b)
        print "Side C is " + str(c)
        self.match = 0
        if a == b:
            self.match = self.match + 1
        if a == c:
            self.match = self.match + 2
        if b == c:
            self.match = self.match + 3
        if self.match == 0:
            if (a + b) <= c:
                self.texto = "NotATriangle"
            elif (b + c) <= a:
                self.texto = "NotATriangle"
            elif (a + c) <= b:
                self.texto = "NotATriangle"
            else:
                self.texto = "Scalene"
        elif self.match == 1:
            if (a + c) <= b:
                self.texto = "NotATriangle"
            else:
                self.texto = "Isosceles"
        elif self.match == 2:
            if (a + c) <= b:
                self.texto = "NotATriangle"
            else:
                self.texto = "Isosceles"
        elif self.match == 3:
            if (b + c) <= a:
                self.texto = "NotATriangle"
            else:
                self.texto = "Isosceles"
        else:
            self.texto = "Equilateral"

        return self.texto

    def getMensaje(self, a, b, c):
        if a < 1 or b < 1 or c < 1:
            raise NumberError('Todos los lados del triangulo deben ser mayor a 1')
        else:
            print "Correcto"


class NumberError(ValueError):
    pass



t = Triangle()
t.getMensaje(2,-3,3)