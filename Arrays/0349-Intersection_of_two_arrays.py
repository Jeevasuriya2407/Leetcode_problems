def intersection(nums1,nums2):
    dict1={}
    dict2={}
    lst=[]
    for i in nums1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for j in nums2:
        if j in dict2:
            dict2[j]+=1
        else:
            dict2[j]=1
    for key,values in dict1.items():
        if key in dict2:
            lst.append(key)
    return lst


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1,nums2))
