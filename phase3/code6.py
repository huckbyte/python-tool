
import unittest

class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)
    
    
class TestIntegerList(unittest.TestCase):
    def _test_intList_IfNotAllInt_RaiseException(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, 2, 3, 4, 5)
        self.assertIsNotNone(context.exception)

    def test_intList_IfAllInt_StoreThem(self):
        values = [1, 2, 3, 4, 5]
        int_list = IntegerList(*values)
        self.assertListEqual(values, int_list.get_data())

    def test_intListAdd_WhenValueIsInt_AddIt(self):
        int_list = IntegerList()
        int_list.add(1)
        self.assertEqual([1], int_list.get_data())

    def test_intListAdd_WhenValueIsNotInt_RaiseException(self):
        int_list = IntegerList()
        with self.assertRaises(Exception) as context:
            int_list.add("string")
        self.assertIsNotNone(context.exception)

    def test_intListRemoveIndex_WhenIndexIsValid_RemoveAndReturnIt(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        returned = int_list.remove_index(3)
        self.assertListEqual([1, 2, 3, 5], int_list.get_data())
        self.assertEqual(4, returned)

    def test_intListRemoveIndex_WhenIndexIsNotValid_RaiseException(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(Exception) as context:
            int_list.remove_index(len(int_list.get_data()))
        self.assertIsNotNone(context.exception)

    def test_intListGet_WhenIndexIsValid_ReturnIt(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        returned = int_list.get(3)
        self.assertEqual(4, returned)

    def test_intListGet_WhenIndexIsNotValid_RaiseException(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(Exception) as context:
            int_list.get(len(int_list.get_data()))
        self.assertIsNotNone(context.exception)

    def test_intListGetBiggest_ReturnMaxElement(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        returned = int_list.get_biggest()
        self.assertEqual(5, returned)

    def test_intListGetIndex_ReturnElementIndex(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        returned = int_list.get_index(1)
        self.assertEqual(0, returned)

    def test_intListInsert_WhenIndexIsValid_InsertIt(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        int_list.insert(2, -1)
        self.assertListEqual([1, 2, -1, 3, 4, 5], int_list.get_data())

    def test_intListInsert_WhenIndexIsNotValid_RaiseException(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(Exception) as context:
            int_list.insert(len(int_list.get_data()), -1)
        self.assertIsNotNone(context.exception)

    def test_intListInsert_WhenValueIsNotInt_RaiseException(self):
        int_list = IntegerList(1, 2, 3, 4, 5)
        with self.assertRaises(Exception) as context:
            int_list.insert(0, "string")
        self.assertIsNotNone(context.exception)


if __name__ == "__main__":
    unittest.main()
