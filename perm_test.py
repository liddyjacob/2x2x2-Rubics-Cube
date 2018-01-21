import unittest

class TestPermutations(unittest.TestCase):

  def test_init(self):
    p1 = permutation([])
    p2 = permutation([(1,2),(1,2)])
    self.assertEqual(p1,p2)

  def test_letter(self):
    p1 = permutation([('x','y','m'),('m','a','w')])
    p2 = permutation([('m', 'a', 'w', 'x', 'y')])
    self.assertEqual(p1,p2)

  
if __name__ == '__main__':
  unittest.main()

