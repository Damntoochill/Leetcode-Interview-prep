dict = {}
for index, val in enumerate(nums):
    if (target-val) in dict:
        return([index,dict[target-val]])
    else:
        dict[val] = index
