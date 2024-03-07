def twoSum(nums,target):
    x = len(nums)
    f = 1
    for i in range(0,x):
        if i < 3 :
            checkSum = nums[i - 1] + nums[i]
            if checkSum == target:
                otvet = [i - 1, i]
                print(otvet)



twoSum([2,7,11,15],9)