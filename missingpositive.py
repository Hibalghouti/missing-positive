def first_missing_positive(numbers):
    
    num_set = set(numbers) #removes duplicate when converting list to a set

    # Start checking from the first positive integer
    for i in range(1, len(numbers) + 1): 
        if i not in num_set:
            return i

print(first_missing_positive([3, 4, -1, 1]))  # Output: 2

