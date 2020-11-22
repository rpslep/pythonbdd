def main():

    print("Social Security Full Retirement Age Calculator")
    y = 1
    m = 0
    while y != 0:
        y = int(input("Enter the year of birth or 0 to exit: "))
        m = int(input("Enter the month of birth: "))
        retirement_calculator(y, m)


def retirement_calculator(year, month):
    retirement_age = 0
    m = 0
    retirement_month = 0
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September"
              , "October", "November", "December"]
    if year <= 1937:
        retirement_age = 65
    elif 1937 < year <= 1942:
        retirement_age = 65
        m = (year - 1937) * 2
    elif 1942 < year <= 1954:
        retirement_age = 66
    elif 1954 < year <= 1959:
        retirement_age = 66
        m = (year - 1954) * 2
    else:
        retirement_age = 67

    retirement_year = year + retirement_age
    if month + m > 12:
        retirement_month = month + m - 12
        retirement_year += 1
    elif month + m == 12:
        retirement_month = 0
        retirement_year += 1
    else:
        retirement_month = month + m

    print("Your full retirement age is: ", retirement_age, " and ", m, " months.")
    print("This will be in ", months[retirement_month - 1], " of ", retirement_year)


main()
