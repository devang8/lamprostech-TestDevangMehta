nums = list(map(int, input()))
target = int(input("Enter target: "))
result = []

for i in range(len(nums)):
    first = nums[i]
    second = nums[i+1]
    if(first + second) == target:   #checking whether elements adds upto the target or not
        result.append(i)
        result.append(i+1)
        print(result)
