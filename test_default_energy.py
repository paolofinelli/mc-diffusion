from nose.tools import assert_true, assert_equal, assert_not_equal, assert_raises
from default_energy import default_energy

def test_energy_known():
    """ test with known result 
        TODO: use proper floating point comparison, make a loop to test over all argument pairs (DRY)
    """
    arguments = [[2], []]
    calc_result = default_energy(arguments[0])
    true_result = 1
    assert_equal(calc_result, true_result)

    arguments = [[2, 3, 4], 2]
    calc_result = default_energy(arguments[0], arguments[1])
    true_result = 20
    assert_equal(calc_result, true_result)

def test_negative_density():
    """ test with a negative element in density vector """
    argument = [1, 1, -1]
    try:
        default_energy(argument)
    except ValueError:
        assert True 

def test_nonint_density():
    """ test with a non-integer element in density vector """
    argument = [1, 0.5]
    try:
        default_energy(argument)
    except TypeError:
        assert True 
