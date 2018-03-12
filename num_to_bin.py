from binary import *

def main():
    input_ints = read_in()
    for i in input_ints:
        print str(binary_to_int(reverse_string(str(int_to_binary(i)))))

if __name__ == '__main__':
    main()
