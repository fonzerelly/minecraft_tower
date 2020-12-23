import unittest

from tower import createTowerAt, createLayerAt

from Position import Position

exact = lambda fst: lambda snd: fst[0] == snd[0] and fst[1] == snd[1] and fst[2] == snd[2]
ignoreHeight = lambda fst: lambda snd: fst[0] == snd[0] and fst[2] == snd[2]
curriedFilter = lambda predicate: lambda l: list(filter(predicate, l))
findExactlyIn = lambda tpl: lambda lst: len(curriedFilter(exact(tpl))(lst)) == 1
excludes = lambda tpl: lambda lst: len(curriedFilter(exact(tpl))(lst)) == 0

class TestCreateTowerAt(unittest.TestCase):

    def test_should_create_tower_at_double_height (self):    
        p = Position()
        singleLayer = createLayerAt(p,0)
        result = createTowerAt(p,2)
        self.assertEqual(len(result), 2*len(singleLayer)-2)

    def test_should_leave_a_door_open(self):
        p = Position()
        result = createTowerAt(p,3)
        self.assertTrue(excludes((0, 0, 2))(result))
        self.assertTrue(excludes((0, 1, 2))(result))
        
class TestCreateLayer(unittest.TestCase):
    def setUp(self):
        p = Position()
        self.resultZero = createLayerAt(p, 0)
        self.resultOne = createLayerAt(p, 1)

    def test_should_position_center_of_tower(self):
        self.assertTrue(findExactlyIn((-1, 0, 4))(self.resultZero))

    def test_should_position_center_according_to_passed_in_position(self):
        p = Position(1, 2, 3)
        result = createLayerAt(p,0)
        self.assertTrue(findExactlyIn((0, 2, 7))(result))

    def test_should_have_wall_to_the_right(self):
        self.assertTrue(findExactlyIn((1, 0, 2))(self.resultZero))
        self.assertTrue(findExactlyIn((1, 0, 3))(self.resultZero))
        self.assertTrue(findExactlyIn((1, 0, 4))(self.resultZero))
        self.assertTrue(findExactlyIn((1, 0, 5))(self.resultZero))
        self.assertTrue(findExactlyIn((1, 0, 6))(self.resultZero))

    def test_should_have_wall_to_the_left(self):
        self.assertTrue(findExactlyIn((-3, 0, 2))(self.resultZero))
        self.assertTrue(findExactlyIn((-3, 0, 3))(self.resultZero))
        self.assertTrue(findExactlyIn((-3, 0, 4))(self.resultZero))
        self.assertTrue(findExactlyIn((-3, 0, 5))(self.resultZero))
        self.assertTrue(findExactlyIn((-3, 0, 6))(self.resultZero))

    def test_should_have_wall_at_back(self):
        self.assertTrue(findExactlyIn((-2, 0, 6))(self.resultZero))
        self.assertTrue(findExactlyIn((-1, 0, 6))(self.resultZero))
        self.assertTrue(findExactlyIn(( 0, 0, 6))(self.resultZero))

    def test_should_have_wall_at_front_with_door(self):
        self.assertTrue(findExactlyIn((-2, 0, 2))(self.resultZero))
        self.assertTrue(findExactlyIn((-1, 0, 2))(self.resultZero))

    def test_should_position_center_of_tower_at_level_one(self):
        self.assertTrue(findExactlyIn((-1, 1, 4))(self.resultOne))

    def test_should_position_center_according_to_passed_in_position_at_lefel_one(self):
        p = Position(1, 2, 3)
        result = createLayerAt(p, 1)
        self.assertTrue(findExactlyIn((0, 3, 7))(result))

    def test_should_have_wall_to_the_right_at_level_one(self):
        self.assertTrue(findExactlyIn((1, 1, 2))(self.resultOne))
        self.assertTrue(findExactlyIn((1, 1, 3))(self.resultOne))
        self.assertTrue(findExactlyIn((1, 1, 4))(self.resultOne))
        self.assertTrue(findExactlyIn((1, 1, 5))(self.resultOne))
        self.assertTrue(findExactlyIn((1, 1, 6))(self.resultOne))

    def test_should_have_wall_to_the_left_at_level_one(self):
        self.assertTrue(findExactlyIn((-3, 1, 3))(self.resultOne))
        self.assertTrue(findExactlyIn((-3, 1, 2))(self.resultOne))
        self.assertTrue(findExactlyIn((-3, 1, 4))(self.resultOne))
        self.assertTrue(findExactlyIn((-3, 1, 5))(self.resultOne))
        self.assertTrue(findExactlyIn((-3, 1, 6))(self.resultOne))

    def test_should_have_wall_at_back_at_level_one(self):
        self.assertTrue(findExactlyIn((-2, 1, 6))(self.resultOne))
        self.assertTrue(findExactlyIn((-1, 1, 6))(self.resultOne))
        self.assertTrue(findExactlyIn(( 0, 1, 6))(self.resultOne))

    def test_should_have_wall_at_front_with_door_at_level_one(self):
        self.assertTrue(findExactlyIn((-2, 1, 2))(self.resultOne))
        self.assertTrue(findExactlyIn((-1, 1, 2))(self.resultOne))

if __name__ == '__main__':
    unittest.main() 