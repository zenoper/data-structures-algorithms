numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    length = len(array) - 1
    for i in array:
        for j in range(length):
            if array[j] > array[j + 1]:
                bubble = array[j]
                array[j] = array[j + 1]
                array[j + 1] = bubble
    return array

print(bubbleSort(numbers))