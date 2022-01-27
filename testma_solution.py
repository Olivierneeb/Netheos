import unittest
from ma_solution import BackwardsSearcher

class TestBackwardsSearcher(unittest.TestCase):

    # def setUp(self):
    #     self.finder = BackwardsSearcher('test_1.pdf')

    def test_1(self):
        BackwardsSearcher('test_1.pdf').block_find_eof()

    def test_2(self):
        BackwardsSearcher('test_2.pdf').block_find_eof()

    def test_3(self):
        BackwardsSearcher('test_3.pdf').block_find_eof()

    def test_4(self):
        BackwardsSearcher('test_4.pdf').block_find_eof()

    def test_6(self):
        BackwardsSearcher('test_6.pdf').block_find_eof()

    def test_7(self):
        BackwardsSearcher('test_beginning.pdf').block_find_eof()

    def test_8(self):
        BackwardsSearcher('test_tricky.pdf').block_find_eof()

if __name__ == '__main__':
    unittest.main()