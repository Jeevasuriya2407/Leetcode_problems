def contains_duplicate(nums):
    dict1={}
    for i in nums:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for key,values in dict1.items():
        if values>=2:
            return True
    return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
