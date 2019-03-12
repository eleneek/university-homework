multi_dimensional_array = [1,[9,[[[[[2]]]]]],[[[2],[12,[2]],[10]]]]


def changeWithRecursion(multi_dimensional_array):
    if multi_dimensional_array == []:
        return multi_dimensional_array
    if isinstance(multi_dimensional_array[0], list):
        return changeWithRecursion(multi_dimensional_array[0]) + changeWithRecursion(multi_dimensional_array[1:])
    return multi_dimensional_array[:1] + changeWithRecursion(multi_dimensional_array[1:])

print(changeWithRecursion(multi_dimensional_array))


def change(multi_dimensional_array):
    new_list = []
    for item in multi_dimensional_array:
        if type(item) != list:
            new_list.append(item)
            print(item)
        else:
            new_list.extend(change(item))
            print(item)
    return new_list

print(change(multi_dimensional_array))