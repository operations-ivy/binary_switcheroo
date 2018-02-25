from binary import *

input_ints = [13, 47]
output_bins = []
for i in input_ints:
    print str(i) + " in binary " + str(int_to_binary(i))
    print str(int_to_binary(i)) + " reversed is " + reverse_string(str(int_to_binary(i)))
    print reverse_string(str(int_to_binary(i))) + " to integer is " + str(binary_to_int(reverse_string(str(int_to_binary(i)))))
    print ""
