
def group_anagrams(strs):
    dict1 = {}

    for i in strs:
        sort1 = "".join(sorted(i))

        if sort1 in dict1:
            dict1[sort1].append(i)
        else:
            dict1[sort1] = [i]

    return list(dict1.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
