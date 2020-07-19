import unittest
import bubblesort


class TestBubbleSort(unittest.TestCase):
    """bubble sort test """

    def test_bubble_sort(self):
        """test bubble sort"""

        before = [4, 3, 2, 1]
        after = bubblesort.bubblesort(before)
        self.assertEqual([1, 2, 3, 4], after, "must sort")

if __name__ == '__main__':
    unittest.main()
