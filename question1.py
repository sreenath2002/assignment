# HASH algorithm function
def hash_algorithm(input_string):
    current_value = 0

    for char in input_string:
        ascii_code = ord(char)  # Get ASCII value of the character
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value

# Given initialization sequence
init_sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

# Split the initialization sequence into steps and calculate the sum
steps = init_sequence.split(',')
total_sum = 0

for step in steps:
    current_value = 0
    for char in step:
        ascii_code = ord(char)  # Get ASCII value of the character
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    
    total_sum += current_value


print("Sum of the results of running the HASH algorithm on each step (including invalid steps):", total_sum)

