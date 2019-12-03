# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end
# of the program that do the following:

# • Print the message, The first three items in the list are:. Then use a slice to print the first three items
# from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice to print three items from the
# middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.

numbers = []
for i in range(0, 20):
    numbers.append(i+1)

print("First three items in the list are:")
print(numbers[slice(3)])

print("Three items from the middle of the list are:")
print(numbers[slice(8, 11)])

print("The last three items in the list are:")
print(numbers[slice(len(numbers)-3, len(numbers))])
