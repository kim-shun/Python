'''
def culculate_average(a,b,c,d,e,f,g):
    average = (a + b + c + d + e + f + g) / 7
    return average


result = culculate_average(2,3,4,5,6,7,8)
print("平均は",result,"です")
'''

def culculate_average(nums, quantity):
    nums_sum = sum(nums)
    average = nums_sum / quantity
    return average


quantity = int(input("数字の個数を決めてください："))

nums = []

for i in range(quantity):
    num = int(input("数字を入力してください："))
    nums.append(num)

result = culculate_average(nums, quantity)
print("平均は",result,"です")


    

