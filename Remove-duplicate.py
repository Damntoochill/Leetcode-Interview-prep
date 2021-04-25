nums = [0,0,1,1,1,2,2,3,3,4]
i = 0
j = 1
l = len(nums)
while(j<l):
  if nums[i] == nums[j]:
    nums.remove(nums[i])
    l-=1
    continue
  j+=1
  i+=1
  print(i,j)
  print(nums)