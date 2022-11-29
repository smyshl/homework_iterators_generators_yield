class FlatIterator:

    def __init__(self, list_of_lists):
        self.main_list_length = len(list_of_lists)
        self.input_list = list_of_lists

    def __iter__(self):
        self.main_list_counter = 0
        self.nested_list_counter = 0
        return self

    def __next__(self):

        if self.main_list_counter == self.main_list_length:
            raise StopIteration

        item = self.input_list[self.main_list_counter][self.nested_list_counter]
        self.nested_list_counter += 1

        if self.nested_list_counter == len(self.input_list[self.main_list_counter]):
            self.main_list_counter += 1
            self.nested_list_counter = 0

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

