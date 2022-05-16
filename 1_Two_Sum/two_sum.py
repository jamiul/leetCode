from timeit import timeit


code1 = """
nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# result = twoSum(nums, target)
# print(result)
"""

code2 = """
nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
    dit = {}
    for i, n in enumerate(nums):
        if n in dit:
            return [dit[n], i]
        dit[target - n] = i
    return []


# result = twoSum(nums, target)
# print(result)
"""

code3 = """
def twoSum(nums, target):
    list = {}
    for index, value in enumerate(nums):
        remainder = target - value
        if remainder in list:
            return [list[remainder], index]
        list[value] = index
"""

print("code1=",timeit(code1, number=1000000))
print("code2=",timeit(code2, number=1000000))
print("code2=",timeit(code3, number=1000000))