import main
import pytest


@pytest.mark.parametrize(["price", "stamp_prices", "expected"], [
    (10, [1, 2, 3], 4),
    (23, [1, 5], 7)
])
def test_get_max_needed_stamps(price, stamp_prices, expected):
    actual = main.get_max_needed_stamps(price, stamp_prices)
    assert expected == actual

