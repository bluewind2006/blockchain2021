import time
from datetime import datetime

POSIX=1530676194171
date='2018-07-04 02:05:46'

print time.mktime(datetime.strptime(date,'%Y-%m-%d %H:%M:%S').timetuple())

datetime.fromtimestamp(1530676194171/1000)