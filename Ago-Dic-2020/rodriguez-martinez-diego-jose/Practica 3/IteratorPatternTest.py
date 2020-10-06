import unittest
from Client import recorrer_iterable
from mArbolBinario import MBTree
from mRange import MRange


class IteratorPatternTest(unittest.TestCase):
    def test_recorrerMyTree(self):
        myTree = MBTree(10)

        for i in range(11,13):
            myTree.insert(i)

        self.assertEqual(recorrer_iterable(myTree), [10,11,12])
    
    def test_recorrerMyTreeUnsorted(self):
        myTree = MBTree(10)

        myTree.insert(1)
        myTree.insert(12)
        myTree.insert(140)

        self.assertEqual(recorrer_iterable(myTree), [1,10,12,140])

    def test_recorrerMyTreeOnlyRoot(self):
        myTree = MBTree(10)

        self.assertEqual(recorrer_iterable(myTree), [10])

    def test_recorrerMyTreeEmpty(self):
        myTree = MBTree()

        self.assertEqual(recorrer_iterable(myTree), [None])
    
    def test_recorrerMyTreeString(self):
        myTree = MBTree("A")

        myTree.insert("B")
        myTree.insert("C")
        myTree.insert("D")
        myTree.insert("E")

        self.assertEqual(recorrer_iterable(myTree), ["A","B","C","D","E"])

    def test_recorrerMyRange(self):
        myRange = MRange(start = 1, stop = 6)

        self.assertEqual(recorrer_iterable(myRange), [1,2,3,4,5])

    def test_recorrerMyRangeEmpty(self):
        myRange = MRange()

        self.assertEqual(recorrer_iterable(myRange), [i for i in range(0,100)])

    def test_NoInterfaceAvailable(self):
        with self.assertRaisesWithMessage(ValueError):
            recorrer_iterable(1)

    #######
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
