import Lab2
import mock

def test_REQ_1():
    result1 = []
    result2 = []
    result3 = []

    input1 = "5,2,22,11,3"
    test1 = [5, 2, 22, 11, 3]
    with mock.patch('builtins.input', return_value=input1):
        assert Lab2.get_user_input() == test1

    input2 = "4,2,3,1,12"
    test2 = [4, 2, 3, 1, 12]
    with mock.patch('builtins.input', return_value=input2):
        assert Lab2.get_user_input() == test2

    input3 = "123,2323,123,2233,144.5"
    test3 = [123, 2323, 123, 2233, 144.5]
    with mock.patch('builtins.input', return_value=input3):
        assert Lab2.get_user_input() == test3

def test_REQ_2():
    input1 = [1, 2, 3, 4, 5]
    test1 = '3.0'
    result1 = Lab2.calc_average_temp(input1)

    input2 = [1, 5, 2, 10, 12]
    test2 = '6.0'
    result2 = Lab2.calc_average_temp(input2)

    input3 = [122.23, 134.23, 343.46, 456.23]
    test3 = '264.04'
    result3 = Lab2.calc_average_temp(input3)

    assert(test1 == result1)
    assert(test2 == result2)
    assert(test3 == result3)