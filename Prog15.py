def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    nums = []

    print("Enter the elements of the array:")
    for _ in range(n):
        nums.append(int(input()))

    result = find_single_number(nums)
    print(f"Output: {result}")
