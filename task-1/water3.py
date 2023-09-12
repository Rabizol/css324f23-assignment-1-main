
def initial_state():
    return (8, 0, 0) #initial bottle water

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    r = 8 - x
    if y > 0 and r > 0:
      if y>r:
        yield ((8, y-r, z), r)
      else :
        yield ((x+y, 0, z), y)
    if z > 0 and r>0:
      if z>r:
        yield ((8, y, z-r), r)
      else :
        yield ((x+z, y, 0), z) 
    r = 5 - y
    if x>0 and r>0:
      if x>r:
        yield ((x-r, 5, z), r)
      else:
        yield ((0, y+x, z), x)
    if z>0 and r>0:
      if z>r:
        yield ((x, 5, z-r), r)
      else:
        yield ((x, y+z, 0), z)
    r = 3 - z
    if x>0 and r>0:
     if x>r:
      yield ((x-r, y, 3), r)
     else:
      yield ((0, y, z+x), x)
    if y>0 and r>0:
     if y>r:
      yield ((x, y-r, 3), r)
     else:
      yield ((x, 0, z+y), y)
