import types


def flat_generator(list_of_lists):

    flat_list = []

    def get_deeper(deep_list):
        nonlocal flat_list

        for deep_item in deep_list:
            if not isinstance(deep_item, list):
                flat_list.append(deep_item)
            elif isinstance(deep_item, list) and len(deep_item) != 0:
                get_deeper(deep_item)
            elif isinstance(deep_item, list) and len(deep_item) == 0:
                break
        return flat_list

    for item in get_deeper(list_of_lists):
        yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
