from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        CS3_Set = Set(["James", "Tony", "Chris", "Sky", "Matthew"])
        DS1_Set = Set(["James", "Matthew", "Tassos", "Sam", "Don"])
        assert CS3_Set.contains("Tony") is True
        assert CS3_Set.contains("Jeff") is False
        assert DS1_Set.contains("Don") is True
        assert DS1_Set.contains("Sky") is False
        assert CS3_Set.size is 5

    def test_add(self):
        CS3_Set = Set(["James", "Tony", "Chris", "Sky", "Matthew"])
        CS3_Set.add("Elliot")
        assert CS3_Set.contains("Elliot") is True
        CS3_Set.remove("Sky")
        assert CS3_Set.contains("Sky") is False

    def test_union(self):
        CS3_Set = Set(["James", "Tony", "Chris", "Sky", "Matthew"])
        DS1_Set = Set(["James", "Matthew", "Tassos", "Sam", "Don"])
        assert CS3_Set.union(DS1_Set).contains(['Tony', 'Sam', 'Don', 'Tassos',
                                                'James', 'Matthew', 'Sky', 'Chris']) is True

    def test_intersection(self):
        CS3_Set = Set(["James", "Tony", "Chris", "Sky", "Matthew"])
        DS1_Set = Set(["James", "Matthew", "Tassos", "Sam", "Don"])
        interSet = CS3_Set.intersection(DS1_Set)
        assert interSet.contains(["James", "Matthew"]) is True
        assert interSet.contains("Tony") is False
        assert interSet.contains("Sam") is False

    def test_is_subset(self):
        Instruct_Set = Set(["Adam", "Eliel", "Alan", "Mike", "Mitchell"])
        DS1_Instruct_Set = Set(["Alan", "Mike"])
        assert Instruct_Set.is_subset(DS1_Instruct_Set) is True

    def test_difference(self):
        Instruct_Set = Set(["Adam", "Eliel", "Alan", "Mike", "Mitchell"])
        DS1_Instruct_Set = Set(["Alan", "Mike"])
        diffSet = DS1_Instruct_Set.difference(Instruct_Set)
        assert diffSet.contains(["Adam", "Eliel", "Mitchell"]) is True
        assert diffSet.contains(["Alan"]) is False
        assert diffSet.contains(["Mike"]) is False
