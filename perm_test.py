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

  def test_order_change(self):
    p1 = Permutation([(1,2,3)])
    p2 = Permutation([(2,3,1)])

    self.assertEqual(p1,p2)

  def test_mult(self):
    p1 = Permutation([(1,2,3)])
    p2 = Permutation([('x','y','z')])
    e  = Permutation([])
    p3 = p1 * p1 * p1 * p2 * p2 * p2
    p4 = p1 * p1 * p2

    self.assertEqual(e, p3)
    self.assertNotEqual(p4, p4 * p4)
    self.assertNotEqual(p4, e)
     
if __name__ == '__main__':
  unittest.main()

