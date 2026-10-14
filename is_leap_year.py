
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0


def main():
    years = [2000, 1900, 2020, 2021, 2024, 2100]
    for year in years:
        print(f"{year} -> {'Leap year' if is_leap_year(year) else 'Not a leap year'}")


if __name__ == "__main__":
    main()
