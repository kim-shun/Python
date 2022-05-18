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
