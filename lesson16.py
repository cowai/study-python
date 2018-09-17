import datetime
import os
import shutil
import time

print('#####################')
now = datetime.datetime.now()
print(now)
print(now.isoformat())
# %f マイクロ秒
print(now.strftime('%d/%m/%y-%H:%M:%S (%f)'))

print('#####################')
today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

print('#####################')
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H:%M:%S (%f)'))

print('#####################')
print(now)
d = datetime.timedelta(weeks=1, days=365, hours=1, minutes=5, seconds=10, microseconds=100)
print(now - d)

print('#####################')
print('###')
print(time.time())
time.sleep(2)
print('###')
print(time.time())

print('#####################')
file_name = 'text.txt'
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y%m%d_%H%M%S')))

with open(file_name, 'w') as f:
    f.write('from lesson16!')
