import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Zero cases
        (0, 0, [0, 0]),
        # Before first milestone (15 years)
        (14, 14, [0, 0]),
        # First milestone (15 years -> 1 human year)
        (15, 15, [1, 1]),
        # Before second milestone (24 years)
        (23, 23, [1, 1]),
        # Second milestone (24 years -> 2 human years)
        (24, 24, [2, 2]),
        # Cat boundary checks (+1 human year for every 4 cat years after 24)
        (27, 24, [2, 2]),  # Cat: 24 + 3 (still 2 human years)
        (28, 24, [3, 2]),  # Cat: 24 + 4 (reaches 3 human years)
        # Dog boundary checks (+1 human year for every 5 dog years after 24)
        (24, 28, [2, 2]),  # Dog: 24 + 4 (still 2 human years)
        (24, 29, [2, 3]),  # Dog: 24 + 5 (reaches 3 human years)
        # Large/Example cases
        (100, 100, [21, 17]),  # Cat: 2 + (76 // 4) = 21 | Dog: 2 + (76 // 5) = 17
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
