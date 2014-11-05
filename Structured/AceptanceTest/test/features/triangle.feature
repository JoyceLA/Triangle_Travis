Feature: Determine the triangle type
	In order to play with Lettuce As beginners We’ll implement factorial

Scenario: Determine the triangle type
	Given I have the integers a = 6 , b = 6 and c = 6
	When I determine triangle type
	Then I see the triangle type "Equilateral"
Scenario: Determine the triangle type
	Given I have the integers a = 6 , b = 9 and c = 5
	When I determine triangle type
	Then I see the triangle type "Scalene"
Scenario: Determine the triangle type
	Given I have the integers a = 6 , b = 3 and c = 6
	When I determine triangle type
	Then I see the triangle type "Isosceles"
Scenario: Determine the triangle type
	Given I have the integers a = 5 , b = 5 and c = 12
	When I determine triangle type
	Then I see the triangle type "Not A Triangle"

