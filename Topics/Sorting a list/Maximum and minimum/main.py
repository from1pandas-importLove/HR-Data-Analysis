# the following code creates a list from input, please do not modify it
ints = [int(num) for num in input().split()]

# your solution here
sorted_reverse_list = sorted(ints, reverse=True)
maximum = sorted_reverse_list[0]
minimum = sorted_reverse_list[-1]
remainder = sorted_reverse_list[1]
print(maximum, minimum, remainder)
