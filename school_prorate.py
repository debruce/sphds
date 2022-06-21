#!env python3

from datetime import date
from datetime import datetime
from datetime import timedelta
from pprint import pprint
from collections import defaultdict

def date_range(s, e=None):
    if isinstance(s, str):
        s = datetime.strptime(s, "%m-%d-%Y").date()
    if e is None:
        return [ s ]
    if isinstance(e, str):
        e = datetime.strptime(e, "%m-%d-%Y").date()
    return [s + timedelta(days=x) for x in range(0, (e-s).days+1)]

school_holidays = [
    *date_range('9-5-2022'),
    *date_range('9-26-2022', '9-27-2022'),
    *date_range('10-4-2022', '10-5-2022'),
    *date_range('10-10-2022', '10-11-2022'),
    *date_range('10-17-2022', '10-18-2022'),
    *date_range('11-11-2022'),
    *date_range('11-18-2022'),
    *date_range('11-22-2022', '11-25-2022'),
    *date_range('12-2-2022'),
    *date_range('12-9-2022'),
    *date_range('12-16-2022'),
    *date_range('12-23-2022', '1-3-2023'),
    *date_range('1-6-2023'),
    *date_range('1-13-2023'),
    *date_range('1-16-2023'),
    *date_range('1-20-2023'),
    *date_range('1-27-2023'),
    *date_range('2-3-2023'),
    *date_range('2-10-2023'),
    *date_range('2-17-2023'),
    *date_range('2-20-2023'),
    *date_range('2-24-2023'),
    *date_range('3-3-2023'),
    *date_range('3-17-2023'),
    *date_range('4-3-2023', '4-14-2023'),
    *date_range('5-26-2023', '5-29-2023'),
]

total_days = 0
school_range = date_range('8-17-2022', '6-14-2023')
per_month_days = defaultdict(int)

for d in school_range:
    if d.weekday() in [ 5, 6 ]:
        continue
    if d in school_holidays:
        continue
    per_month_days[d.month] += 1
    total_days += 1

pprint(per_month_days)
print()

remaining_days = total_days

for d in school_range:
    if d.weekday() in [ 5, 6 ]:
        continue
    if d in school_holidays:
        continue
    percentage = 100.0 * remaining_days / total_days
    print(f'{d} {remaining_days:3d} {percentage:6.2f}')
    remaining_days -= 1
