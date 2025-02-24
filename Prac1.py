def sort_numbers_and_names(numbers, names):
    # Sort the numbers list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Calculate the sum of the numbers
    total_sum = sum(sorted_numbers)
    
    # Sort the names list in alphabetical order
    sorted_names = sorted(names)
    
    return sorted_numbers, total_sum, sorted_names


# Example input lists
numbers = [2, 12, 89, 23, 67, 5]
names = ["Tahmid", "Sasha", "Maria", "Anjl", "Adi"]

# Call the function and get the sorted results
sorted_numbers, total_sum, sorted_names = sort_numbers_and_names(numbers, names)

# Print the sorted lists and the sum
print("Sorted Numbers:", sorted_numbers)
print("Sum of Numbers:", total_sum)
print("Sorted Names:", sorted_names)

