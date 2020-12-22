import unittest

from tower import createTowerAt

from Position import Position

def exact (list):
    filter(lambda t: t[0] == )

class TestCreateTowerAt(unittest.TestCase):
    def setUp(self):
        p = Position()
        self.resultBottom = createTowerAt(p)

    def test_should_position_center_of_tower(self):
        self.resultBottom.index((-1, 0, 4))

    def test_should_position_center_according_to_passed_in_position(self):
        p = Position(1, 2, 3)
        result = createTowerAt(p)
        result.index((0, 2, 7))

    def test_should_have_wall_to_the_right(self):
        self.resultBottom.index((1, 0, 2))
        self.resultBottom.index((1, 0, 3))
        self.resultBottom.index((1, 0, 4))
        self.resultBottom.index((1, 0, 5))
        self.resultBottom.index((1, 0, 6))

    def test_should_have_wall_to_the_left(self):
        self.resultBottom.index((-3, 0, 2))
        self.resultBottom.index((-3, 0, 3))
        self.resultBottom.index((-3, 0, 4))
        self.resultBottom.index((-3, 0, 5))
        self.resultBottom.index((-3, 0, 6))

    def test_should_have_wall_at_back(self):
        self.resultBottom.index((-2, 0, 6))
        self.resultBottom.index((-1, 0, 6))
        self.resultBottom.index(( 0, 0, 6))

    def test_should_have_wall_at_front_with_door(self):
        self.resultBottom.index((-2, 0, 2))
        self.resultBottom.index((-1, 0, 2))

    
    

if __name__ == '__main__':
    unittest.main() 