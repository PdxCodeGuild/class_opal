# Lab 13: Compass

Copy the [compass module](13_compass.py) in this folder. Fill in code in each place that has `...` to make the methods work. Run your file with `pytest` to make sure all the tests pass. Don't change the tests! 

The class represents a compass. The compass has only one attribute, a `heading`, or direction in degrees. North is 0 degrees, east is 90, south is 180, east is 270. 

There is also a `get_direction` method that gets the associated cardinal direction of that heading, and a `turn` method that turns the compass left or right by a specified amount.

Override the built in `__add__` and `__sub__` dunder methods to add custom behavior when a heading would go over 360 or below zero. Override the `__eq__` method to return True when two compasses with the same heading are compared. 

Note: The dunder methods are available as `self.__method__` but you can't rely on their behavior being implemented inside the class definition. Using the `+`, `-`, or `==` operators may not work the way you have specified. Only the `__str__` method will definitely work inside the class definition. 