class LinearSearch:
    def __init__(self, data):
        self.data = data
    
    def search_element(self, target):
        for i in range(len(self.data)):
            if self.data[i] == target:
                return i
        return -1

# Creating an object of the LinearSearch class
numbers = [10, 25, 36, 47, 58, 69, 80]
search_obj = LinearSearch(numbers)

# Taking user input for the search element
target = int(input("Enter number to search: "))

result = search_obj.search_element(target)

# Displaying the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")