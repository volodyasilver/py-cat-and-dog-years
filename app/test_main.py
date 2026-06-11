import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        # Cat boundary checks
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),
        # Dog boundary checks
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        # Very large age/Extreme inputs
        (1000, 1000, [246, 197]),
    ]
)
def test_get_human_age_valid_ranges(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 5),
        (5, -1),
        (-100, -100),
    ]
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
    ]
)
def test_get_human_age_invalid_types(cat_age: any, dog_age: any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
