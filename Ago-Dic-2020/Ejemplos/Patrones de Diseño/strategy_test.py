import pytest

from strategy import BubbleSortConcreteStrategy, MergeSortConcreteStrategy, QuickSortConcreteStrategy, SortContext

@pytest.mark.parametrize("items, expected", [
    (
        [i for i in range(0, 100)],
        "Ordenando con bubble sort!"
    ),
    (
        [i for i in range(0, 10000)],
        "Ordenando con merge sort!"
    ),
    (
        [i for i in range(0, 100000)],
        "Ordenando con quick sort!"
    )
])
def test_defaults(items, expected):
    context = SortContext(items)
    assert context.sort_context() == expected

@pytest.mark.parametrize("concrete_strategy, expected", [
    (
        BubbleSortConcreteStrategy(),
        "Ordenando con bubble sort!"
    ),
    (
        MergeSortConcreteStrategy(),
        "Ordenando con merge sort!"
    ),
    (
        QuickSortConcreteStrategy(),
        "Ordenando con quick sort!"
    )
])
def test_specifics(concrete_strategy, expected):
    context = SortContext([1, 9, 8, 3, 55], concrete_strategy)
    assert context.sort_context() == expected
    
@pytest.mark.parametrize("concrete_strategy_1, concrete_strategy_2, expected_1, expected_2", [
    (
        BubbleSortConcreteStrategy(),
        MergeSortConcreteStrategy(),
        "Ordenando con bubble sort!",
        "Ordenando con merge sort!",
    ),
])
def test_updating_strategy(concrete_strategy_1, concrete_strategy_2, expected_1, expected_2):
    context = SortContext([1, 9, 8, 3, 55], concrete_strategy_1)
    assert context.sort_context() == expected_1
    
    context.set_strategy(concrete_strategy_2)
    assert context.sort_context() == expected_2