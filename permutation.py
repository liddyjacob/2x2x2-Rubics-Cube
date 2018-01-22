
#### Permutations ##
## The permutations are what will govern the calculation behind turning
## the rubiks cube. It is a permutation in the traditional mathematics
## sense, and is described in disjoint cycle notation. For more 
## information, here is the wikipedia article: 
# https://en.wikipedia.org/wiki/Permutation #

import permUtils

class Permutation:

  # Cycles will be in any form, so they must be simplified.
  def __init__(self, cycles):
    self.cycles = permUtils.simplify(cycles)

  # Multiplication is done by listing cycles and permuting
  # from left to right.
  def __mul__(self, other):
    return Permutation(self.p1 + self.p2)

  # A permutation is defined by its cycles.
  def __str__(self):
    return str(self.cycles)

