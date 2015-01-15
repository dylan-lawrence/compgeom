import random
import math

from my_modules.geom.point import Point

class utils:
  '''This class will only contain static methods'''

  @staticmethod
  def pointsInCircle(radius, numPoints, centerPt=(0,0), seed=None):
    '''This returns a random point in the unit circle'''
    rand = random.Random(seed)
    points = []
    for i in range(numPoints):
      #simple circle generator, we're using trig here and then pretending we didn't
      angle = rand.random() * math.pi * 2
      rad = rand.randrange(radius + 1)
      x = centerPt[0] + int(rad * math.cos(angle))
      y = centerPt[1] + int(rad * math.sin(angle))
      points.append(Point(x,y))

    return points

  @staticmethod
  def pointDirection (p1,p2,p3):
    '''Checks if three points move clockwise'''
    '''returns < 0 for counterclockwise, > 0 for clockwise, and 0 for co-linear'''
    return ((p2.getX() - p1.getX()) * (p3.getY() - p1.getY())) - ((p2.getY() - p1.getY()) * (p3.getX() - p1.getX()))
