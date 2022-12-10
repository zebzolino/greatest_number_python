# Open the text file in read mode
with open('numbers.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the contents into a list of numbers
numbers = [int(x) for x in contents.split()]

# Print the largest number in the list
print(max(numbers))
