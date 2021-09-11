def culculate_average(nums, quantity):
    nums_sum = sum(nums)
    average = nums_sum / quantity
    return average

try:
    def input_num():
        quantity = int(input("数字の個数を決めてください："))
        nums = []
        for i in range(quantity):
            num = int(input("数字を入力してください："))
            nums.append(num)
        result = culculate_average(nums, quantity)
        print("平均は",result,"です")

    input_num()
    
except ZeroDivisionError:
    print("ゼロはだめよ")
    input_num()
except ValueError:
    print("数字ではありませんよ")
    input_num()
