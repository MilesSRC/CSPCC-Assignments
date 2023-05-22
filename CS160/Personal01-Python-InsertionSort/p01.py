# Insertion Sorting
def main():
    arr = [2, 5, 3, 7, 4, 9, 6, 39, 371, 274, 297, 90, 93745, 37, 58];

    for index in range(1, len(arr)):
        j = index - 1;
        current = arr[index];

        while j > 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1;
        
        arr[j + 1] = current

    print(arr)
    return arr;

main();