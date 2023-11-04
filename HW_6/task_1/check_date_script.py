import check_date
import sys

date_to_check = sys.argv[1]
if check_date.check_date(date_to_check):
    print('Дата корректна!')
else:
    print('Дата не корректна!')
