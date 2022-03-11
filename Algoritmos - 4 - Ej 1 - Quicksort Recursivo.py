def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smaller = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)

print(quicksort([2,11,34,54,9,6,35,87,12,33]))
