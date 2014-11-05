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

    def getMensaje(self, a, b, c):
        if a<1  or b < 1 or c < 1:
            raise NumberError('Todos los lados del triangulo deben ser mayor a 1')
        else:
            print "Correcto"

class NumberError(ValueError):
    pass


t = Triangle()
t.getMensaje(2,-3,3)