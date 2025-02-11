def find_max(list):
    max_index = 0
    for j in range(len(list)):
        if list[j] > list[max_index]:
            max_index = j
    print(max_index)

# test
find_max([1, 3, 6, 8, 0])