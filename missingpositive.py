def first_missing_positive(numbers):

    # Start checking from the first positive integer
    for i in range(1, len(numbers) + 1): 
        if i not in numbers:
            return i

print(first_missing_positive( [1, 2, 0]))
print(first_missing_positive(  [3, 4, -1, 1]))  

