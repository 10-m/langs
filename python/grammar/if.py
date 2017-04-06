now = int(input("now? "))
if (now > 18) or (now < 5):
    print("night")
elif (now < 11):
    print("mornig")
elif now == 12:
    print("noon")
elif (now > 12) and (now < 17):
    print("afternoon")
else:
    print("evening")

year = int(input("Year? "))
is_leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

if is_leap:
    print(str(year) + " is leap year,")
else:
    print(str(year) + " is not leap year,")
