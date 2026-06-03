from collections import namedtuple
color = (55,155,255)
print (color[0])



#USING NAMEDTUPLE

color = namedtuple('color',['red','green','blue'])
color = color(55,125,blue=44)
print (color.green)