from datetime import date


def days_diff(start, end):
    return (end - start).days


days_diff(date(2022, 10, 25), date(2022, 12, 25))

print(days_diff(date(2022, 10, 25), date(2022, 12, 25))) # 61
