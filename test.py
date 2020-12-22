import unittest

from tower import createTowerAt

from Position import Position



exact = lambda fst: lambda snd: fst[0] == snd[0] and fst[1] == snd[1] and fst[2] == snd[2]
curriedFilter = lambda predicate: lambda l: list(filter(predicate, l))
findExactlyIn = lambda tpl: lambda lst: len(curriedFilter(exact(tpl))(lst)) == 1

class TestCreateTowerAt(unittest.TestCase):
    def setUp(self):
        p = Position()
        self.resultBottom = createTowerAt(p)

    def test_should_position_center_of_tower(self):
        self.assertTrue(findExactlyIn((-1, 0, 4))(self.resultBottom))

    def test_should_position_center_according_to_passed_in_position(self):
        p = Position(1, 2, 3)
        result = createTowerAt(p)
        self.assertTrue(findExactlyIn((0, 2, 7))(result))

    def test_should_have_wall_to_the_right(self):
        self.assertTrue(findExactlyIn((1, 0, 2))(self.resultBottom))
        self.assertTrue(findExactlyIn((1, 0, 3))(self.resultBottom))
        self.assertTrue(findExactlyIn((1, 0, 4))(self.resultBottom))
        self.assertTrue(findExactlyIn((1, 0, 5))(self.resultBottom))
        self.assertTrue(findExactlyIn((1, 0, 6))(self.resultBottom))

    def test_should_have_wall_to_the_left(self):
        self.assertTrue(findExactlyIn((-3, 0, 2))(self.resultBottom))
        self.assertTrue(findExactlyIn((-3, 0, 3))(self.resultBottom))
        self.assertTrue(findExactlyIn((-3, 0, 4))(self.resultBottom))
        self.assertTrue(findExactlyIn((-3, 0, 5))(self.resultBottom))
        self.assertTrue(findExactlyIn((-3, 0, 6))(self.resultBottom))

    def test_should_have_wall_at_back(self):
        self.assertTrue(findExactlyIn((-2, 0, 6))(self.resultBottom))
        self.assertTrue(findExactlyIn((-1, 0, 6))(self.resultBottom))
        self.assertTrue(findExactlyIn(( 0, 0, 6))(self.resultBottom))

    def test_should_have_wall_at_front_with_door(self):
        self.assertTrue(findExactlyIn((-2, 0, 2))(self.resultBottom))
        self.assertTrue(findExactlyIn((-1, 0, 2))(self.resultBottom))

    
    

if __name__ == '__main__':
    unittest.main() 