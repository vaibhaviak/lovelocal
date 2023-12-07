from collections import Counter

def majorityElement(nums):
  n = len(nums)
  count_map = Counter(nums)
  majority_element = n // 3
  result = []
  for num, count in count_map.items():
    if count > majority_element:
      result.append(num)
  return result

# User input
nums_str = input("Input: ")

# Convert string input to list of integers
nums = []
for x in nums_str.strip('[]').split(","):
  nums.append(int(x))

# Print the result
print("output:",majorityElement(nums))