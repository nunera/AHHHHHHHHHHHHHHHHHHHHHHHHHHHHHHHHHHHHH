# Michael Kryvonis Period 10

# Subprograms
def leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return 0
    elif year % 4 == 0:
        return 1
    else:
        return 0

def number_of_days(month, year):
    if month == 2:
        if leap_year(year) == 1:
            return 29
        else:
            return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30

def days_passed(day,month,year):
    for i in range(1,month):
        day += number_of_days(i,year)
    return day - 1


print("Please enter a date")
d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))
menu = int(input("""Menu:
1) Calculate the number of days in the given month.
2) Calculate the number of days passed in the given year.\n"""))
if menu == 1:
    print(number_of_days(m,y))
elif menu == 2:
    print(days_passed(d,m,y))
else:
    print("stop")
