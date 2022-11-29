class FlatIterator:

    def __init__(self, list_of_lists):
        self.input_list = list_of_lists.copy()

    def __iter__(self):
        return self

    def __next__(self):

        if len(self.input_list) == 0:
            raise StopIteration

        while self.input_list:
            item = self.input_list.pop(0)
            if isinstance(item, list) and len(item) != 0:
                self.input_list[:0] = item
            else:
                if item == []:
                    raise StopIteration
                return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
