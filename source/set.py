from hashtable import HashTable


class Set(object):
    """Set Class."""

    def __init__(self, elements = None):
        self.setItems = HashTable()
        self.size = 0
        if elements:
            for element in elements:
                self.add(element)

    def contains(self, element):
        if isinstance(element, list):
            for item in element:
                if not self.setItems.get(item):
                    return False
            return True
        else:
            if self.setItems.get(element):
                return True
            else:
                return False

    def add(self, element):
        self.setItems.set(element, True)
        self.size += 1

    def remove(self, element):
        self.setItems.delete(element)
        self.size -= 1

    def union(self, other_set):
        newSet = Set(self.setItems.keys())
        for element in other_set.setItems.keys():
            if not newSet.contains(element):
                newSet.add(element)
        return newSet

    def intersection(self, other_set):
        newSet = Set()
        for element in self.setItems.keys():
            if other_set.contains(element):
                newSet.add(element)
        return newSet

    def difference(self, other_set):
        newSet = Set()
        for element in other_set.setItems.keys():
            if not self.contains(element):
                newSet.add(element)
        return newSet

    def is_subset(self, other_set):
        for element in other_set.setItems.keys():
            if not self.contains(element):
                return False
        return True
