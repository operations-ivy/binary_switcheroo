import sys

def read_in():
    return {x.strip() for x in sys.stdin}

def int_to_string(incoming_int):
    outgoing_int = str(incoming_int)
    return outgoing_int

def reverse_string(incoming_str):
    outgoing_str = incoming_str[::-1]
    return outgoing_str

def int_to_binary(incoming_int):
    outgoing_bin = "{0:b}".format(int(incoming_int))
    return outgoing_bin

def binary_to_int(incoming_bin):
    outgoing_int = int(incoming_bin, 2)
    return outgoing_int
