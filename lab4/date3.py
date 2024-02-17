from datetime import datetime

def drop_microseconds(dt):
    return dt.replace(microsecond=0)

original = datetime.now()
datetime_without_microseconds = drop_microseconds(original)

print(datetime_without_microseconds)