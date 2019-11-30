import apps.factorial as fact
import pytest


@pytest.mark.parametrize("value, ret_value, msg",
                         [
                             (4, 24, 'values are not equal'),
                             (4, 25, 'values are not equal'),
                             (0, 0, 'values are not equal'),
                             (-1, 'INVALID NUMBER', 'values are not equal')])
def test_positive_scenario_1(value, ret_value, msg):
    assert fact.validate_factorial(value) == ret_value, msg
