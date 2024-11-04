def first_missing_positive(numbers):
    #removes duplicate when converting list to a set
    num_set = set(numbers) 

    # Start checking from the first positive integer
    for i in range(1, len(numbers) + 1): 
        if i not in num_set:
            return i

print(first_missing_positive([3, 4, -1, 1]))

