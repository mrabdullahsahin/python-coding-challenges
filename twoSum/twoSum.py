class Solution:
    def twoSum(nums,target):
        i = 0
        j = 1
        while i < len(nums):
            j = 1
            while j < len(nums):
                if i != j:
                    if (target == (nums[i] + nums[j])):
                        return [i,j]
                    else:
                        j += 1
                else:
                    j += 1
            i += 1


count = int(input("How many numbers do you want to enter: "))
i = 0
numbers = []
while i < count:
    while True:
        number = input("please enter the enter the number: ")
        if number.isnumeric():
            break
    numbers.append(int(number))
    i += 1

while True:
    targetNumber = input("Which number do you want the sum of two?: ")
    if number.isnumeric():
        break

print(numbers)
result = Solution.twoSum(numbers,targetNumber)
print(result)