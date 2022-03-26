import datetime
import calendar

def create_calendar(date):

    month_name = ["","January","February","March","April","May","June",
            "July","August","September","October","November","December"]

    print("   ",month_name[date.month],date.year)

    print("Su Mo Tu We Th Fr Sa")

    week_num = [1,2,3,4,5,6,0]
    first_day_week = datetime.date(date.year,date.month,1).weekday()
    _, lastday = calendar.monthrange(date.year, date.month)

    print("%2s " % ' ' * week_num[first_day_week],end='')
    for i in range(1,lastday + 1):
        print("%2d " % i,end='')
        if (week_num[first_day_week] + i) % 7 == 0:
            print()
    print('\n')



now = datetime.datetime.now() #2022-03-26 14:58:27.351358
today = datetime.date(now.year,now.month,now.day)
april = datetime.date(2022,4,5)
may = datetime.date(2022,5,5)

create_calendar(today)
create_calendar(april)
create_calendar(may)

#weekday()メソッドで、月曜日が0で日曜日が6
#isoweekday()があるが、こちらは月曜日が1で日曜日が7
#今回日曜日から土曜



