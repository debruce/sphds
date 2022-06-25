#!env python3

from pprint import pprint
from pathlib import Path
import pygsheets
from collections import defaultdict
from datetime import datetime
from datetime import date
import time

client_secret = Path.home() / 'client_id.json'
gc = pygsheets.authorize(client_secret=client_secret.as_posix(), credentials_directory=Path.home().as_posix())

doc_name = 'test_sheet2'

try:
    sheet = gc.open(doc_name)
    print('opened old file')
except:
    sheet = gc.create(doc_name)
    print('opened new file')

# print(f'list of sheets = {sheet.worksheets()}')
# for wks in sheet.worksheets():
#     wks.update_row(5, [datetime.now().strftime("%m/%d/%Y, %H:%M:%S")])


wks = sheet.worksheet()

cells = wks.find('gloom')
for cell in cells:
    print(f'row = {cell.row}, col = {cell.col}, color={cell.color}')
    cell.color = (1,0,0,1)
    cell.set_value(cell.value.upper())
wks.update_cells(cells)

# wks.update_row(1, ['Room', 'doom', 'gloom'])


# print("got sheets")
# wks = sheet.worksheet_by_title('For Hang\'s use only : Original Order from parents ')
# for_billing = sheet.worksheet_by_title('Weekly Meal Count ')

# form2room = {
#     'Summer Camp Room 1- 18 months to 2 years old': '1',
#     'Summer Camp Room 2 - 2-3 years old': '2',
#     'Summer Camp Room  5 - PreK class 5 years old': '5',
#     'Summer Camp Room 6 - 4 years old': '6',

# }

# data = defaultdict(lambda : dict())

# for r in range(2,wks.rows):
#     row = wks.get_row(r)
#     if row[0] == '':
#         break
#     ts, child, room, diet_note = row[0:4]
#     child = child.lower()
#     if room in form2room:
#         room = form2room[room]
#     lunches = [row[x] for x in range(4,9)]
#     other_note = row[9]
#     print(f'room = "{room}", child = "{child}", lunches = {lunches} diet={diet_note} other_note={other_note}')
#     try:
#         prior_lunches, prior_diet, prior_other = data[room][child]
#         for i in range(5):
#             if prior_lunches[i] == 'Yes':
#                 lunches[i] = 'Yes'
#         if len(prior_diet) > 0:
#             diet_note = prior_diet + ' / ' + diet_note
#         if len(prior_other) > 0:
#             other_note = prior_other + ' / ' + other_note
#     except:
#         pass
#     data[room][child] = (lunches, diet_note, other_note)

# print()
# print()
# for_billing.clear()
# for_billing.update_row(1, ['Room', 'Child', 'Wk2', 'Wk3', 'Wk4', 'Wk5', 'Wk6', 'Dietary notes', 'Other notes'])

# row_num = 2
# lunch_sum = [ 0, 0, 0, 0, 0 ]
# for rm, children in sorted(data.items()):
#     print(f'{rm}')
#     for child, rec in sorted(children.items()):
#         print(f'    {child:20s} Lunches={rec[0]} Dietary="{rec[1]}" Other="{rec[1]}"')
#         contents = [rm, child]
#         contents += rec[0]
#         contents.append(rec[1])
#         contents.append(rec[2])
#         for_billing.update_row(row_num, contents)
#         for idx in range(5):
#             if rec[0][idx] == 'Yes':
#                 lunch_sum[idx] += 1
#         row_num += 1
#     print()

# row_num += 1
# for_billing.update_row(row_num, ['Total', '', *lunch_sum, '', ''])
