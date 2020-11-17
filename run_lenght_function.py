from collections import OrderedDict


def run_length_encoding(input_code):
    # Generate ordered dictionary of all lower case alphabets
    dictionary = OrderedDict.fromkeys(input_code, 0)

    # Now iterate through input string to calculate frequency of each character
    for ch in input_code:
        dictionary[ch] += 1

    # now iterate through dictionary to make output string from (key,value) pairs
    output = ''
    for key, value in dictionary.items():
        output = output + key + str(value)
    return output


# MAIN
input_to_encode = "AAAAWWAAAAEEEETT"
print(input)
output_coded = run_length_encoding(input_to_encode)
print(output_coded)

