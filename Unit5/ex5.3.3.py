def show_date(day, month, year=17):
    print(day, "/", month, "/", year)


show_date(day=15, month=12, year=17) # 15 / 12 / 17

show_date(month=15, day=12) # 15 / 12 / 17

show_date(17, 12) # 12 / 15 / 17

show_date(15, year=12) # Type error