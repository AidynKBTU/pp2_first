import datetime

def date_difference_in_seconds(date1, date2):
    timedelta = date2 - date1
    return abs(timedelta.total_seconds())

date1 = datetime.datetime.now()
date2 = date1 + datetime.timedelta(days=1)

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)
