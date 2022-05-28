number_N = int(input('Введите количество элементов списка: '))
nums = []
value = 1
for i in range(1, number_N + 1):
    nums.append(value)
    value *= i + 1
print(nums)