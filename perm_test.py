import unittest
import permutation

Permutation = permutation.Permutation


class TestPermutations(unittest.TestCase):

  def test_init(self):
    p1 = Permutation([])
    p2 = Permutation([(1,2),(1,2)])
    self.assertEqual(p1,p2)

  def test_letter(self):
    p1 = Permutation([('x','y','m'),('m','a','w')])
    p2 = Permutation([('m', 'a', 'w', 'x', 'y')])
    self.assertEqual(p1,p2)

  
if __name__ == '__main__':
  unittest.main()

