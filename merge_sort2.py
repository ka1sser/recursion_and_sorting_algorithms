def merge_sort(items):

    # Base Case
    if len(items) <= 1:
        return items

    # Splitting into 2 lists
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    # Recursive call
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    """Helper function to handle the arranging and merging after it is splitted"""

    result = []

    # This will continue until a side has no more value left
    while left and right:

        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)

        else:
            result.append(right[0])
            right.pop(0)

    # This will add the remaining values to the list
    if left:
        result += left
    if right:
        result += right

    return result


unordered_list1 = [
    "Itadori",
    "Edward",
    "Bojji",
    "Alphonse",
    "Kuroku",
    "Kage",
    "Gojo",
    "Megumi",
]

unordered_list2 = [123, 92, 17, 341, 571, 891, 21, 89, 431, 267, 12, 53]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)

print(ordered_list1)
print(ordered_list2)
