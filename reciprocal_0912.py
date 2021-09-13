def caluculate_reciprocal():
    nums = []
    i =0
    while sum(nums) < 7:
        reciprocal = 1 / i
        nums.append(reciprocal)
        i+= 1
    print(sum(nums))
    print(len(num))

try:
    caluculate_reciprocal()
except ZeroDivisionError:
    print("ゼロはだめよ")
