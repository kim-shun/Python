num = 3
num_type = type(num)
print(num_type)

if num_type == int:
    print("intだよ")
else:
    print("intジャない")

a = ""

if a is None:
    print("ない")
else:
    print("ある")

dict = {}

print(dict)
if dict is None:
    print("ぺ")
else:
    print("あ")

if len(dict) == 0:
    print("ない")
else:
    print("ある")

dicttest = [{'message':'こんにちは','code':'AA'},{'message':'こんばんは','code':'BB'}]
print(dicttest)

for dict in dicttest:
    print(dict)
    print(dict['message'])
    
   
