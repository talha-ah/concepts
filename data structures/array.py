# python saves the pointers to the actual values of the array in memory
# deleting an element (say at the start) is a linear time O(n)
# inserting an element (say at the start) is a linear time O(n)
# appending an element (at the end) is a constant time O(1)
# searching an element is a linear time O(n)

new_list = [1, 2, 3]

result = new_list[0]  # constant time

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

new_list.append(4)
new_list.extend([5, 6, 7])
print(new_list)
