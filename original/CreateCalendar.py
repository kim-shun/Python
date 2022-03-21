import datetime

today = datetime.date(2022, 3, 21)
month_name = ["","January","February","March","April","May","June",
	"July","August","September","October","November","December"]

print("   ",month_name[today.month],today.year)

print("Su Mo Tu We Th Fr Sa")

first_day_week = datetime.date(2022,3,1).weekday() + 1
print("%2s " % ' ' * first_day_week,end='')
for i in range(1,32):
    print("%2d " % i,end='')
    if (first_day_week + i) % 7 == 0:
        print()





