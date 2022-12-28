nums = list(map(int, input()))
target = int(input())
result = []
for i in range(nums + 1):
  if(nums[i] + nums[i + 1]) == target:   #checking whether the indices of the list adds upto the target
    result.append(i)
    result.append(i + 1)
print(result)
