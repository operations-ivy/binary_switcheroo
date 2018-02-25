from binary import *
import nose

test_binary = "1000101"
test_int = 69
test_string = "danzig"
good_int = 4990864642
bad_int = 10000000000

def test_int_to_string():
    assert int_to_string(test_int) == "69"

def test_reverse_string():
    assert reverse_string(test_string) == "giznad"

def test_int_to_binary():
    assert int_to_binary(test_int) == test_binary

def test_binary_to_int():
    assert binary_to_int(test_binary) == test_int

#def test_int_length():
#    assert length_checker(good_int) == good deal


if __name__ == '__main__':
    nose.run()
