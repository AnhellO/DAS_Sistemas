import unittest
from Client import recorrerIterable
from mArbolBinario import mBTree
from mRange import mRange


class IteratorPatternTest(unittest.TestCase):
    def test_recorrerMyTree(self):
        myTree = mBTree(10)

        for i in range(11,13):
            myTree.insert(i)

        self.assertEqual(recorrerIterable(myTree), [10,11,12])
    
    def test_recorrerMyTreeUnsorted(self):
        myTree = mBTree(10)

        myTree.insert(1)
        myTree.insert(12)
        myTree.insert(140)

        self.assertEqual(recorrerIterable(myTree), [1,10,12,140])

    def test_recorrerMyTreeOnlyRoot(self):
        myTree = mBTree(10)

        self.assertEqual(recorrerIterable(myTree), [10])

    def test_recorrerMyTreeEmpty(self):
        myTree = mBTree()

        self.assertEqual(recorrerIterable(myTree), [None])
    
    def test_recorrerMyTreeString(self):
        myTree = mBTree("A")

        myTree.insert("B")
        myTree.insert("C")
        myTree.insert("D")
        myTree.insert("E")

        self.assertEqual(recorrerIterable(myTree), ["A","B","C","D","E"])

    def test_recorrerMyRange(self):
        myRange = mRange(start = 1, stop = 6)

        self.assertEqual(recorrerIterable(myRange), [1,2,3,4,5])

    def test_recorrerMyRangeEmpty(self):
        myRange = mRange()

        self.assertEqual(recorrerIterable(myRange), [i for i in range(0,100)])

    def test_NoInterfaceAvailable(self):
        with self.assertRaisesWithMessage(ValueError):
            recorrerIterable(1)

    #######
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
