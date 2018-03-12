from binary import *
import nose

test_binary = "10001111"
test_int = 143
test_string = "danzig"

def test_int_to_string():
    assert int_to_string(test_int) == "143"

def test_reverse_string():
    assert reverse_string(test_string) == "giznad"

def test_int_to_binary():
    assert int_to_binary(test_int) == test_binary

def test_binary_to_int():
    assert binary_to_int(test_binary) == test_int

if __name__ == '__main__':
    nose.run()
