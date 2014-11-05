# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append("../")
from Triangle import Triangle

@step(u'Given I have the integers a = (\d+) , b = (\d+) and c = (\d+)')
def given_i_have_the_number1_number2(step, a, b, c):
    world.number = [int(a),int(b),int(c)]

@step(u'When I determine triangle type')
def when_i_determine_triangle_type(step):
	triangle = Triangle()
	world.type = triangle.setSides(world.number[0],world.number[1],world.number[2])

@step(u'Then I see the triangle type "([^"]*)"')
def then_i_see_the_number_1(step, expected):
    assert world.type == expected, "Resultado {0} and {1}".format(world.type,expected)
