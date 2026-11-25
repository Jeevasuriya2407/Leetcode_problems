def top_k_frequent(nums, k):
    dict1 = {}

    for i in nums:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    sorted_elements = sorted(dict1, key=dict1.get, reverse=True)
    print(sorted_elements)
    return sorted_elements[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(top_k_frequent(nums, k))
