from datetime import datetime


def main():
    my_time = datetime.now()
    print(my_time)

    my_day = datetime.today()
    print(my_day)
    print(f"Year: {my_day.year}")
    print(f"Month: {my_day.month}")
    print(f"day: {my_day.day}")

    # %Y = Year
    # %m = Month
    # %d = Day
    # %H = Hour
    # %M = Minute
    # %S = Second

    my_datetime = datetime.now()
    print(my_datetime)

    my_str = my_datetime.strftime("%d/%m/%Y")
    print(f"Formato LATAM: {my_str}")

    my_str = my_datetime.strftime("%m/%d/%Y")
    print(f"Formato USA: {my_str}")

    my_str = my_datetime.strftime("Estamos en el año %Y")
    print(f"Formato Random: {my_str}")


if __name__ == "__main__":
    main()
