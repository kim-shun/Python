def cal_hexa(num):
    nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hexa = ""
    while num:
        remainder = num % 16
        
        hexa = nums[remainder] + hexa
        num //= 16
    return hexa

print(cal_hexa(160)) #A0
print(cal_hexa(100)) #64
print(cal_hexa(50)) #32
print(cal_hexa(7770))
